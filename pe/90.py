from numbert import bindigits
from itertools import combinations

def fill(a,b):
    num=set([x for x in range(10)])
    an=6-len(a)
    bn=6-len(b)
    ad=num-a
    bd=num-b
    a_all=combinations(ad,an)
    b_all=list(combinations(bd,bn))
    for k in a_all:
        for m in b_all:
            ar=list(a|set(k))
            br=list(b|set(m))
            ar.sort()
            br.sort()
            ar=tuple(ar)
            br=tuple(br)
            yield ar+br
'''a=set([x for x in range(6)])
print(a)
for p in fill(a,a):
    print(p)'''

def produce():
    for i in range(512):
        print('i is'+str(i))
        a=[0,0,0,1,2,3,4,6,8]
        b=[1,4,6,6,5,6,6,4,1]
        ibi=bindigits(i,9)
        ibi=list(str(ibi))
        for j in range(len(ibi)):
            if ibi[j]=='1':
                temp=a[j]
                a[j]=b[j]
                b[j]=temp
        a1=set(a)
        b1=set(b)
        if len(a1)<=6 and len(b1)<=6:
            for n in fill(a1,b1):
                yield n
            if 6 in a1:
                a2=set(a1)
                a2.remove(6)
                a2.add(9)
                for n1 in fill(a2,b1):
                    yield n1
            if 6 in b1:
                b2=set(b1)
                b2.remove(6)
                b2.add(9)
                for n2 in fill(a1,b2):
                    yield n2
            if 6 in b1 and 6 in a1:
                for n3 in fill(a2,b2):
                    yield n3
res=set()
res2=set()
counter=0
for q in produce():
    res.add(q)
print(len(res)/2)
    
