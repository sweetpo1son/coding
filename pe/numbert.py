if __name__ == '__main__':
    pass
    
def pl(x):
    res=[2]
    def test_all(y,z):
        for j in z:
            if y%j==0:
                return False
        return True
    for i in range (3,x):
        if test_all(i,res):
            res.append(i)
    return res

def factors_partition(n, I=2):
    import math
    yield (n,)
    for i in range(I, int(math.sqrt(n)) + 1):
        if n%i==0:
            for p in factors_partition(int(n/i), i):
                yield (i,) + p
def partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def factors(n):
    s=set([1])
    from math import sqrt
    for k in range(2,int(sqrt(n))+1):
        if n%k==0:
            s.add(k)
            s.add(n//k)
    return s
#print(factors(9))
def factors_y(n):
    yield 1
    from math import sqrt
    for k in range(2,int(sqrt(n))+1):
        if n%k==0:
            yield k
            yield n//k
    if n==int(sqrt(n))**2:
        yield -int(sqrt(n))

def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


def factorise(n):
    from math import sqrt
    d={}
    div=2
    while n>1:
        if n%div==0:
            if div in d:
                d[div]+=1
            else:
                d[div]=1
            n=n//div
            div=2
        else:
            if div>sqrt(n):
                if n in d:
                    d[n]+=1
                else:
                    d[n]=1
                break
            else:
                div+=1
    return d