import time
s89=set([89])
s1=set([1])
result=0

def ds2(n):
    res=0
    n=list(str(n))
    for i in range(len(n)):
        d=int(n.pop())
        res+=d**2
    return res

for i in range(1,568):
    print(i)
    d=i
    while True:
        d=ds2(d)
        if d in s89:
            s89.add(i)
            break
        if d in s1:
            s1.add(i)
            break
        
print('done')

l=[ds2(x) for x in range(100000)]


for k in range(0,100):
    print(k)
    base=ds2(100000*k)
    for m in l:
        if (base+m) in s89:
            result+=1
print(result)
