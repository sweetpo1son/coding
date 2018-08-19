
import urllib.request
from bs4 import BeautifulSoup
import re

upperMB=30
numb=2

def downld(u,ind):
    #import time
    global upperMB
    import urllib.request
    from bs4 import BeautifulSoup
    import re
    import requests

    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=u, headers=headers)
    with urllib.request.urlopen(req) as url:
        s=url.read()
    soup = BeautifulSoup(s)
    typ = soup.find(text=re.compile("epub|mobi|pdf|djvu"))
    big = soup.find(text=re.compile("bytes"))

    for t in soup.find_all('input'):
        try:
            title=t['value']
            print(title)
        except KeyError:
            pass
    print(big)
    print(typ)
    big=str(big)
    sta=big.find('(')
    end=big.find(')')-6
    bigness=int(big[(sta+1):end])
    print(bigness)
    if bigness>1024*1024*30:
        print('too big, abort')
        return 'abort'
    if ind ==2:
        ds2 = soup.find(href=re.compile('^ed2k'))
        print(ds2['href'])
        return(ds2['href'])
    if ind ==3:
        li3='no'
        firsthead3='torrent=$'
        for ds3 in soup.find_all(href=re.compile(firsthead3)):
            print(ds3)
            li3=ds3['href']
            break
        li3="http://gen.lib.rus.ec"+li3


        
        r = requests.get(li3,verify=False)

        with open(title+'.torrent','wb') as f:
            f.write(r.content)
    if ind==1:
        firsthead="libgen.io/ads"
        # firsthead="/item/adv/"
        #firsthead='library1.ga/_ads'
        secondhead="dl4.libgen.io/get"
        #secondhead="/download/book/"
        li='no'
        for ds in soup.find_all(href=re.compile(firsthead)):
            li=ds['href']
            break
        
        #li="download1."+li[7:] #optional!!!!
        print(li)                                    
        req1=urllib.request.Request(url=li,headers=headers)
        with urllib.request.urlopen(req1) as url1:
            s1=url1.read()
        soup1 =BeautifulSoup(s1)
        fileurl=''

        for ks in soup1.find_all(href=re.compile(secondhead)):
            fileurl=ks['href']
            break
        

        print(fileurl)

        r = requests.get(fileurl, stream=True,verify=False)
        with open(title, "wb") as pdf:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)
                '''
        r = requests.get(fileurl,verify=False)

        with open(title,'wb') as f:
            f.write(r.content)
            '''



ur='http://gen.lib.rus.ec/search.php?req='
#bk="introduction to analysis"

bk="theory of relativity"
bk=bk.split()
add='+'.join(bk)
link=ur+add

print(link)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=link, headers=headers)
with urllib.request.urlopen(req) as url:
    smain=url.read()

soup = BeautifulSoup(smain)
#text=str(soup.get_text())
#print(text)

for d in soup.find_all('tr'):
    print()
    counter=1
    for ds in d.find_all(href=re.compile("book/index.php"),limit=numb):
        l=ds['href']
        l='http://gen.lib.rus.ec/'+l
        print(l)
        downld(l,1)
        print(str(counter)+' book done')
        counter+=1
        

                
'''
a='http://libgen.io/book/index.php?md5=B2EA561BBFA3BCE030AE58B7241AE36D'
b="https://libgen.pw/item/detail/id/5a1f049e3a044650f5019160"
c="https://libgen.pw/item/detail/id/5a1f04f33a044650f508b07f"
d="http://gen.lib.rus.ec/book/index.php?md5=A20331129AFF4B9CF9CFBFD6A11451B1"
downld(d,2)
'''