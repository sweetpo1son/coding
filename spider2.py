
user3=''
u_plus=""


import urllib.request
from bs4 import BeautifulSoup
import re
import time
user3_uni=user3.encode()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
res=[]
time1=time.time()
for i in range(1,500):
    if i%50==0:
        time2=time.time()
        print(str(time2-time1)+' seconds')
        print(res)
        time.sleep(10)
    u=u_plus+str(i)
    req = urllib.request.Request(url=u, headers=headers)
    with urllib.request.urlopen(req) as url:
        s = url.read()
    soup = BeautifulSoup(s)
    text=str(soup.get_text())
    text_uni=text.encode()
    try:
        a=re.search(user3_uni,text_uni).span()
    except AttributeError:
        print(str(i)+" pass")
        continue
    else:
        print('OK')
        res.append(str(i))
print(res)
time2=time.time()
print(str(time2-time1)+' seconds')