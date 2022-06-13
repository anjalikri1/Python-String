s=input("enter ths string :")
l=s.split()
i=0
l1=[]
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    if i%2!=0:
        l1.append(l[i][::-1])
    i+=1
print(l1)
op=" ".join(l1)
print(op)