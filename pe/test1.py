import math
import time
def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n

for n in range(1,300):
    print(n)
    sq=3*n**2-2
    if isSqr(sq):
        print(n)
        print(sq)
        time.sleep(5)