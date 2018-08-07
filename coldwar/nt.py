

def prime_list_exclu(x):
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
     