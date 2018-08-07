import math
from nt import prime_list_exclu
list=prime_list_exclu(7072)
s=set()
def find_break(bound,list):
    for i in range(len(list)):
        if list[i]>=bound:
            return i
    return len(list)
fiftymillion=50*1000*1000
bound3=math.ceil(math.pow(fiftymillion,0.25))
res=0
for j in range(find_break(bound3,list)):
    print('j is '+str(j))
    part2=math.pow(list[j],4)
    diff2=fiftymillion-part2
    print('diff 2 is '+str(diff2))
    bound2=math.ceil(math.pow(diff2,(1/3)))
    print('bound 2 is '+str(bound2))
    for k in range(find_break(bound2,list)):
        print('k is '+str(k))
        part1=math.pow(list[k],3)
        diff1=diff2-part1
        print('diff1 is '+str(diff1))
        bound1=math.ceil(math.sqrt(diff1))
        print('bound 1 is '+str(bound1))
        for l in range(find_break(bound1,list)):
            s.add(part2+part1+math.pow(list[l],2))
print(len(s))
