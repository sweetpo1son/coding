d1={'IV':2, 'IX':2, 'XL':20, 'XC':20, 'CD':200, 'CM':200}
d2={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def cal(s):
    res=0
    for i in d2:
        res+=s.count(i)*d2[i]
    for j in d1:
        res-=s.count(j)*d1[j]
    return res

def digi(di,li):
    res=''
    di=int(di)
    if di<4:
        res=li[0]*di
    else:
        if di==4:
            res=li[0]+li[1]
        else:
            if di<=8:
                res=li[1]+li[0]*(di-5)
            else:
                res=li[0]*(10-di)+li[2]
    return res
def roma(n):
    n=list(str(n))
    while len(n)<4:
        n.insert(0,'0')
    res1='M'*int(n[0])
    res2=digi(n[1],['C','D','M'])
    res3=digi(n[2],['X','L','C'])
    res4=digi(n[3],['I','V','X'])
    res=res1+res2+res3+res4
    return res


li=[]
chara=0
f=open('p089_roman.txt','r')
for line in f.readlines():
    line=line.strip()
    chara+=len(line)
    chara-=len(roma(cal(line)))
f.close
print(chara)