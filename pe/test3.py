from numbert import factorise,factors_y
import time

def sum_of_factors(x):
  return sum([n for n in range(1,x) if x % n == 0])
def factorsum(n):
    res=1
    d=factorise(n)
    for j in d:
        res*=(j**(d[j]+1)-1)//(j-1)
    return res-n

def factorsum1(n):
    res=0
    for k in factors_y(n):
        res+=k
    return res
t1=time.time()
print(factorsum1(102222))
print(time.time()-t1)


t2=time.time()
print(factorsum(102222))
print(time.time()-t2)