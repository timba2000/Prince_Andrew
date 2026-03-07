#!/usr/bin/env python3
import sqlite3, requests, json, time, re
from concurrent.futures import ThreadPoolExecutor, as_completed
DB='/data/.openclaw/workspace/dive_sites.db'
CONC=12
HEADERS={'User-Agent':'SDU-Heavy/1.0'}
DOMAINS=['wikipedia.org','tripadvisor.','scubadiving','diveplanet','diving.net.au','marinas','geonames','osm.org','austlii','gov.au']


def get_targets():
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute("SELECT ID,Name,Region,Latitude,Longitude FROM dive_sites WHERE validation_status IN ('needs_review','needs_web_corroboration')")
    rows=cur.fetchall()
    conn.close()
    return rows


def search_html(q):
    try:
        r=requests.post('https://duckduckgo.com/html/', data={'q':q}, headers=HEADERS, timeout=15)
        if r.status_code==200:
            return r.text
    except:
        return ''
    return ''


def extract_links(html):
    return re.findall(r'href=["\']([^"\']+)["\']', html)


def analyze(target):
    sid,name,region,lat,lon=target
    info={'id':sid,'name':name,'found':[],'status':'needs_review','evidence':[]}
    queries=[f"{name} {region} site", f"{name} dive site {region}", f"{name} wreck {region}", f"{name} jetty {region}"]
    for q in queries:
        html=search_html(q)
        links=extract_links(html)
        low=html.lower()
        for d in DOMAINS:
            if d in low:
                info['found'].append(d)
        # also collect distinct absolute links that look relevant
        for link in links[:10]:
            if any(d in link for d in DOMAINS) or name.replace(' ','').lower()[:6] in link.lower():
                info['evidence'].append(link)
        if info['found']:
            info['status']='corroborated_auto'
            break
    if not info['found']:
        if info['evidence']:
            info['status']='needs_review'
        else:
            info['status']='needs_web_corroboration'
    return info


def update_db(conn,info):
    cur=conn.cursor()
    cur.execute('UPDATE dive_sites SET validation_status=? WHERE ID=?',(info['status'],info['id']))
    conn.commit()


def main():
    targets=get_targets()
    print('targets',len(targets))
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

if __name__=='__main__':
    main()
