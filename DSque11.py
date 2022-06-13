s="a3d4w2c5"
target=""
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        target=target+x*d
op="".join(sorted(target))
print(op)
