#!/usr/bin/env python3
import sqlite3, requests, json, time, csv
from concurrent.futures import ThreadPoolExecutor, as_completed

DB='/data/.openclaw/workspace/dive_sites.db'
CSV='/data/.openclaw/workspace/sdu_manual_review.csv'
CONC=8
HEADERS={'User-Agent':'SDU-DeepDive/1.0'}
SOURCES=['scubadiving','diveplanet','tripadvisor','wikipedia','osm.org','marinas','geonames','diving.net.au','seawater','austlife']


def ddg_search(q):
    try:
        r=requests.post('https://duckduckgo.com/html/', data={'q':q}, headers=HEADERS, timeout=12)
        if r.status_code==200:
            return r.text
    except:
        return ''
    return ''


def process_entry(entry):
    sid, name, region, lat, lon, status = entry
    info={'id':sid,'name':name,'found':[], 'status':None}
    queries=[f"{name} {region} dive", f"{name} dive site", f"{name} wreck", f"{name} {region}"]
    for q in queries:
        html=ddg_search(q)
        low=html.lower()
        for s in SOURCES:
            if s in low:
                info['found'].append(s)
        if info['found']:
            info['status']='corroborated_auto'
            break
    if not info['found']:
        info['status']='needs_review'
    return info


def load_targets(n=25):
    entries=[]
    with open(CSV) as f:
        r=csv.DictReader(f)
        for i,row in enumerate(r):
            if i>=n: break
            entries.append((int(row['ID']), row['Name'], row['Region'], row['Latitude'], row['Longitude'], row['validation_status']))
    return entries


def update_db(conn, info):
    cur=conn.cursor()
    cur.execute('UPDATE dive_sites SET validation_status=? WHERE ID=?',(info['status'], info['id']))
    conn.commit()


def main():
    targets=load_targets(25)
    conn=sqlite3.connect(DB)
    results=[]
    with ThreadPoolExecutor(max_workers=CONC) as ex:
        futures={ex.submit(process_entry,t):t for t in targets}
        for f in as_completed(futures):
            try:
                res=f.result()
            except Exception as e:
                t=futures[f]
                res={'id':t[0],'name':t[1],'found':[],'status':'error','err':str(e)}
            results.append(res)
            update_db(conn,res)
            with open('/data/.openclaw/workspace/sdu_progress.log','a') as L:
                L.write(json.dumps(res)+"\n")
    conn.close()
    print(json.dumps({'status':'done','processed':len(results)}))

if __name__=='__main__':
    main()
