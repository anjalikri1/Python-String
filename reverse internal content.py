s=input("enter ths string :")
l=s.split()
print(l)
l1=[]
for w in l:
    l1.append(w[::-1])
print(l1)
op=" ".join(l1)
print(op)

