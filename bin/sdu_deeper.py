#!/usr/bin/env python3
import sqlite3, requests, json, time
from concurrent.futures import ThreadPoolExecutor, as_completed

DB = '/data/.openclaw/workspace/dive_sites.db'
LIMIT = 50
CONCURRENCY = 6
HEADERS={'User-Agent':'SDU-Deep/1.0'}

def get_targets(conn, limit):
    cur=conn.cursor()
    cur.execute("SELECT ID, Name, Latitude, Longitude, Region FROM dive_sites WHERE validation_status IN ('needs_web_corroboration','needs_review') LIMIT ?",(limit,))
    return cur.fetchall()

def ddg_search(query):
    try:
        url = 'https://duckduckgo.com/html/'
        r = requests.post(url, data={'q': query}, headers=HEADERS, timeout=12)
        if r.status_code==200:
            return r.text
    except Exception as e:
        return ''
    return ''

KNOWN_SOURCES = ['diveplanet', 'diving.net.au', 'divingwiki', 'scubadiving', 'tripadvisor', 'wikipedia', 'geonames', 'osm.org']

def analyze(site):
    sid, name, lat, lon, region = site
    res={'id':sid,'name':name,'status':'needs_review','notes':[]}
    q = name + (' '+region if region else '')
    html = ddg_search(q)
    hits = []
    for s in KNOWN_SOURCES:
        if s in html.lower():
            hits.append(s)
    if hits:
        res['status']='corroborated_auto'
        res['notes'].append('found_sources:'+','.join(hits))
    else:
        res['status']='needs_review'
        res['notes'].append('no_known_sources')
    return res

def update_db(conn,res):
    cur=conn.cursor()
    cur.execute('UPDATE dive_sites SET validation_status=? WHERE ID=?',(res['status'],res['id']))
    conn.commit()

def main():
    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row
    targets=get_targets(conn,LIMIT)
    if not targets:
        print(json.dumps({'status':'none'})); return
    print(json.dumps({'status':'processing','count':len(targets)}))
    results=[]
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures={ex.submit(analyze,t):t for t in targets}
        for f in as_completed(futures):
            try:
                r=f.result()
            except Exception as e:
                t=futures[f]
                r={'id':t[0],'name':t[1],'status':'error','notes':[str(e)]}
            results.append(r)
            update_db(conn,r)
            with open('/data/.openclaw/workspace/sdu_progress.log','a') as L:
                L.write(json.dumps(r)+"\n")
    conn.close()
    print(json.dumps({'status':'done','processed':len(results)}))

if __name__=='__main__':
    main()
