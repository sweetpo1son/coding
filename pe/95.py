from numbert import factorise


def factorsum(n):
    res=1
    d=factorise(n)
    for j in d:
        res*=(j**(d[j]+1)-1)//(j-1)
    return res-n

n=1
while True:
    print(n)
    factorsum(n)
    n+=1
    
    '''

d={}
se=set()
for i in range(12,13):
    print(i)
    if i in se:
        continue
    chain=[i]
    while True:
        s=factorsum(chain[-1])
        if s>1000**2 or s in se:
            break       
        flag=True
        for j in range(len(chain)):
            if chain[j]==s:
                d[s]=len(chain)-j
                for q in chain[j:]:
                    print(q)
                    se.add(q)
                flag=False
                break
        if flag:
            chain.append(s)
        else:
            break
start=max(d,key=d.get)
print(d)
'''
