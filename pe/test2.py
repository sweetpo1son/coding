def factors(n):
    s=set([1])
    from math import sqrt
    for k in range(2,int(sqrt(n))+1):
        if n%k==0:
            s.add(k)
            s.add(n//k)
    return s
print(sum(factors(28)))