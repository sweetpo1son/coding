from itertools import permutations
from itertools import combinations
import time
ten=[x for x in range(10)]
max=0
maxnum=0


def chain(lis):
    for i in range(len(lis)):
        if lis[i]!=i+1:
            return i
    return len(lis)
    
def addtail(out,j):
    try:
        out=out+j[2:]
    except IndexError:
        pass
    return out
def generat(li):
    res=[]
    for j in li:
        out1=[j[0]+j[1]]
        res.append(addtail(out1,j))
        out2=[j[0]-j[1]]
        res.append(addtail(out2,j))
        out3=[j[0]*j[1]]
        res.append(addtail(out3,j))
        try:
            out4=[j[0]/j[1]]
            res.append(addtail(out4,j))
        except ZeroDivisionError:
            pass
        out5=[j[1]-j[0]]
        res.append(addtail(out5,j))
        try:
            out6=[j[1]/j[0]]
            res.append(addtail(out6,j))
        except ZeroDivisionError:
            pass
    return res


for k in combinations(ten,4):
    result=set()
    for p in permutations(k,4):
        li=[list(p)]
        li1=generat(li)
        li2=generat(li1)
        li3=generat(li2)
        for i in li3:
            f=i[0]
            if f>0 and int(f)==f:
                result.add(f)
    result=list(result)
    result.sort()
    c=chain(result)
    print(result)
    print(c)
    if k==(1,2,3,4):
        time.sleep(10)
    if c>max:
        max=c
        maxnum=k
print(max)
print(maxnum)