import math

def factors(n, I=2):
    yield (n,)
    for i in range(I, int(math.sqrt(n)) + 1):
        if n%i==0:
            for p in factors(int(n/i), i):
                yield (i,) + p

def find_all(upper):
    li=[ 0 for x in range(upper+1)]
    num=4
    count=0
    s=set()
    while True:
        print(num)
        for i in factors(num):
            ind=num-sum(i)+len(i)
            if ind<=upper and li[ind]==0 :
                li[ind]=num
                count+=1
                s.add(num)
                print('count is '+str(count)+" num "+str(num))
                if count==upper:
                    return s        
        num+=1
print(sum(find_all(12000)))