#!/usr/bin/env python3
import sqlite3, requests, json, time
from concurrent.futures import ThreadPoolExecutor, as_completed

DB = '/data/.openclaw/workspace/dive_sites.db'
BATCH = 50
CONCURRENCY = 10

HEADERS = {'User-Agent': 'SDU-Corroborator/1.0 (+https://example)'}

def get_sites(conn, limit):
    cur = conn.cursor()
    cur.execute("SELECT ID, Name, Latitude, Longitude FROM dive_sites WHERE (validation_status IS NULL OR validation_status LIKE 'needs%') OR validation_status = 'corroboration_in_progress' LIMIT ?", (limit,))
    return cur.fetchall()

def reverse_geocode(lat, lon):
    try:
        url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}&zoom=14'
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        return None
    return None

def check_site(site):
    sid, name, lat, lon = site
    result = {'id': sid, 'name': name, 'status': 'needs_review', 'notes': []}
    if lat is None or lon is None:
        result['status'] = 'missing_or_invalid_coords'
        result['notes'].append('no coordinates')
        return result
    geo = reverse_geocode(lat, lon)
    if not geo:
        result['status'] = 'needs_web_corroboration'
        result['notes'].append('reverse geocode failed')
        return result
    display = geo.get('display_name','').lower()
    if name and name.lower() in display:
        result['status'] = 'corroborated_auto'
        result['notes'].append(f"matched display: {display}")
    else:
        result['status'] = 'needs_review'
        result['notes'].append(f'display: {display}')
    # include OSM url
    osm = geo.get('osm_id')
    if osm:
        result['notes'].append('osm:'+str(osm))
    return result


def update_db(conn, res):
    cur = conn.cursor()
    now = int(time.time())
    status = res['status']
    cur.execute('UPDATE dive_sites SET validation_status = ? WHERE ID = ?', (status, res['id']))
    # optional: store evidence in a separate table
    conn.commit()


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    sites = get_sites(conn, BATCH)
    if not sites:
        print(json.dumps({'status':'no_sites'}))
        return
    print(json.dumps({'status':'processing','count':len(sites)}))
    results = []
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures = {ex.submit(check_site, s): s for s in sites}
        for f in as_completed(futures):
            try:
                r = f.result()
            except Exception as e:
                r = {'id': futures[f][0], 'name': futures[f][1], 'status':'error', 'notes':[str(e)]}
            results.append(r)
            update_db(conn, r)
            # append a log line for the watcher
            with open('/data/.openclaw/workspace/sdu_progress.log','a') as L:
                L.write(json.dumps({'id':r['id'],'name':r['name'],'status':r['status'],'notes':r['notes']})+"\n")
    conn.close()
    print(json.dumps({'status':'done','processed':len(results)}))

if __name__=='__main__':
    main()
