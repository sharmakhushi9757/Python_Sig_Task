#Ques-1:
def Mul(l):
    res=1
    for i in l:
        res*=i
    return res

l=[3,4,5,6,7]
print("Result: ",Mul(l))