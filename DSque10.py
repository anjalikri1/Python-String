str=input("enter the string where alphabet symbol should be followed by digit:")
op=""
for ch in str:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        op=op+x*d
print(op)