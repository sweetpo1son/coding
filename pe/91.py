import math
side=50
result=3*(side**2)

def search(a):
    res=0
    midpoint=(a[0]/2,a[1]/2)
    lengths=(a[0]*a[0]+a[1]*a[1])/4
    for i in range(1,a[0]):
        height=math.sqrt(lengths-(i-midpoint[0])**2)+midpoint[1]
        if height<=side and height==int(height):
            res+=1
    return res
for j in range(1,side+1):
    for k in range(side+1):
        result+=search((j,k))*2
print(result)
            
    
