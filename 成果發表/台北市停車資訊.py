import re
import requests

def 擷取網頁(url):
    global st
# https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json
    s=requests.get(url)
    if s.status_code==200:
        print(f'網頁擷取成功:{s.status_code}')
        st=s.text
        print(st)
    else:
        print(f'網頁擷取失敗:{s.status_code}')
def 查找標題(r):
    p=r'<title>(.+?)</title>'
    m=re.search(p, r)
    print(f'標題:{m.group(1)}')
    return m.group(1)
def 存取網頁內容(r):
    p=r'"contentUrl":"(.+).json"'
    m=re.findall(p, r)
    url=m[0][0:67]
    print(f'點擊網址下載:{url}')
    return url
def 存檔html(file):
    with open(file,'w',encoding='utf-8')as f:
        s=f.write(st)
        print(f'存檔成功,檔名: {file}')
    return s
def 讀取html內容(file):
    with open(file,'r',encoding='utf-8')as f:
        r=f.read()
    print(f'成功讀取: {file}')
    return r
def 自動下載json檔案(url):
    global t
    c=requests.get(url)
    t=c.text
    print('網址下載成功,格式為.json')
def 存檔json檔案(file_name):
    with open(file_name,'w',encoding='utf-8')as f:
        s=f.write(t)
    print(f'存檔成功,檔名: {file_name}')

# 擷取網頁('https://data.gov.tw/dataset/128435')
# file=查找標題()
# 存檔html(f'{file}.html')
g_file= '臺北市停車場資訊 ｜ 政府資料開放平臺.html'
g_r=讀取html內容(g_file)
g_url=存取網頁內容(g_r)
g_name=自動下載json檔案(g_url)
存檔json檔案('臺北市停車場資訊.json')


