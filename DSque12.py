s="aaabbbnnnzcc"
p=s[0]
op=""
c=1
i=1
while i<len(s):
    if s[i]==p:
        c+=1
    else:
        op=op+str(c)+p
        p=s[i]
        c=1
    if i==len(s)-1:
        op=op+str(c)+p
    i+=1
print(op)
