#x^2-3*y^2=1

#x^2-3y^2=-2

#2d+1=y^2

#p=12d+2=6*(y**2)-4

#x=2,y=1
#p=12y**2+4<1000**3
#y<9129
'''
import math
def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n
li2=[]
for n in range(1,300):
    #print(n)
    sq=3*n**2-2
    if isSqr(sq):
        li2.append((int(math.sqrt(sq)),n))
print(li2)

'''
x=2
y=1
res=0
li=[]
for b in range(10):
    li.append((x,y))
    temp=x
    x=2*x+3*y
    y=2*y+temp
#print(res)
print(li)
for x in li:
    if x[1]<=9128:
        print(x)
        res+=12*(x[1]**2)+4
    
p=1
q=1
li3=[]
for i in range (len(li)):
    li3.append((p,q))
    p=li[i][0]+li[i][1]*3
    q=sum(li[i])

print(li3)

for y in li3:
    if y[1]<=12909:
        print(y)
        res+=6*(y[1]**2)-4
print(res-2)
##(1,1) d=0 is not a triangle
 