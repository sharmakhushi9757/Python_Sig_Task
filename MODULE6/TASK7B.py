#Ques-2:
def chk(r,n):
    for i in range(r+1):
        if(i==n):
            return True

r=20
n=2
print("No. is Present or not: ",chk(r,n))