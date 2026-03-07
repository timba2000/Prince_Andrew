#!/usr/bin/env python3
import sqlite3, requests, json, re
from concurrent.futures import ThreadPoolExecutor, as_completed
DB='/data/.openclaw/workspace/dive_sites.db'
KEYWORDS=['wreck','reef','jetty','harbour','pier']
CONC=8
HEADERS={'User-Agent':'SDU-Priority/1.0'}
DOMAINS=['wikipedia.org','tripadvisor.','scubadiving','diveplanet','diving.net.au','osm.org']

def get_targets(limit=50):
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    q='''SELECT ID,Name,Region,Latitude,Longitude FROM dive_sites 
         WHERE (validation_status IN ('needs_review','needs_web_corroboration')) 
         AND ('''+ ' OR '.join([f"Name LIKE '%{k.title()}%'" for k in KEYWORDS]) +''') LIMIT ?'''
    cur.execute(q,(limit,))
    rows=cur.fetchall(); conn.close(); return rows

def search_html(q):
    try:
        r=requests.post('https://duckduckgo.com/html/', data={'q':q}, headers=HEADERS, timeout=15)
        if r.status_code==200: return r.text
    except: return ''
    return ''

def analyze(target):
    sid,name,region,lat,lon=target
    info={'id':sid,'name':name,'found':[], 'status':'needs_review','evidence':[]}
    queries=[f"{name} {region} dive site", f"{name} wreck", f"{name} reef", f"{name} jetty"]
    for q in queries:
        html=search_html(q)
        low=html.lower()
        for d in DOMAINS:
            if d in low:
                info['found'].append(d)
        # collect a few links
        links=re.findall(r'href=["\']([^"\']+)["\']', html)
        for link in links[:6]:
            if any(d in link for d in DOMAINS) or name.replace(' ','').lower()[:6] in link.lower():
                info['evidence'].append(link)
        if info['found']:
            info['status']='corroborated_auto'
            break
    if not info['found'] and info['evidence']:
        info['status']='needs_review'
    if not info['found'] and not info['evidence']:
        info['status']='needs_web_corroboration'
    return info

def update_db(conn,info):
    cur=conn.cursor(); cur.execute('UPDATE dive_sites SET validation_status=? WHERE ID=?',(info['status'],info['id'])); conn.commit()

if __name__=='__main__':
    targets=get_targets(50)
    print('Processing',len(targets),'priority sites')
    conn=sqlite3.connect(DB)
    results=[]
    with ThreadPoolExecutor(max_workers=CONC) as ex:
        futures={ex.submit(analyze,t):t for t in targets}
        for f in as_completed(futures):
            try:
                r=f.result()
            except Exception as e:
                t=futures[f]
                r={'id':t[0],'name':t[1],'status':'error','evidence':[str(e)]}
            results.append(r)
            update_db(conn,r)
            with open('/data/.openclaw/workspace/sdu_progress.log','a') as L:
                L.write(json.dumps(r)+"\n")
    conn.close()
    print(json.dumps({'status':'done','processed':len(results)}))
