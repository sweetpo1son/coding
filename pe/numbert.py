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

def factors(n, I=2):
    yield (n,)
    for i in range(I, int(math.sqrt(n)) + 1):
        if n%i==0:
            for p in factors(int(n/i), i):
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