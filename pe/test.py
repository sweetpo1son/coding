def chain(lis):
    for i in range(len(lis)):
        if lis[i]!=i+1:
            return i
print(chain([0,1.0,2,3,4,5,6,9]))