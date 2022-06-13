
# i/p:-
# s1="abcdefg"
# s2="xyz"
# s3="12345"
# o/p:-
# ax1,by2,cz3,d4,e5.f,g

s1="abcdefg"
s2="xyz"
s3="12345"
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    op=""
    if i<len(s1):
        op=op+s1[i]
        i+=1
    if j<len(s2):
        op=op+s2[j]
        j+=1
    if k<len(s3):
        op=op+s3[k]
        k+=1
    print(op,end=", ")
    
    

    