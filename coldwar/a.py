def out(a):
    if a=='&':
        return lambda x,y:x and y
    if a=='|':
        return lambda x,y: x or y
    if a=='^':
        return lambda x,y: (x or y)and (not(x and y))
def solve(s,ops):
    res=0
    s=list(s)
    for x in range(len(s)):
        if s[x] == 't':
            s[x]=True
        else:
            s[x]=False
    print(s)
    print(ops)
    if len(ops)==1:
        if out(ops[0])(s[0],s[1]):
            return 1
    
    for i in range(len(s)-1):
        s1=s[:i]+[out(ops[i])(s[i],s[i+1])]+s[i+2:]
        ops1=ops[:i]+ops[i+1:]
        res+=solve(s1,ops1)
    return res
print (solve('tft','^&'))
