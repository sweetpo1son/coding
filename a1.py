def out(a):
    if a=='&':
        return lambda x,y:x&y
    if a=='|':
        return lambda x,y: x|y
    if a=='^':
        return lambda x,y:x^y
def bo(s):
    s=list(s)
    for x in range(len(s)):
        if s[x] == 't':
            s[x]=True
        else:         
            s[x]=False
    return s

def solve(s,ops):
    res=0
    if s[0]=='t' or s[0]=='f':
        s=bo(s)
    if len(ops)==1:
        if out(ops[0])(s[0],s[1]):
            return 1
    
    for i in range(len(s)-1):
        first=s[:i]
        second=[out(ops[i])(s[i],s[i+1])]
        third=s[i+2:]
        s1=first+second+third
        ops1=ops[:i]+ops[i+1:]
        res+=solve(s1,ops1)
    return res
print (solve('ttftff','|&^&&'))
