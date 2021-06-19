num=int(input("Enter number of words inserted in lists here"))
l=[]
for i in range(0,num):
    s=input("Enter string here : ")
    l.append(s)
l2=[]
for i in l:
    l2.append(len(i))
l2.sort()
print(l2[-1])
