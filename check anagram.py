s1=input("enter string ")
s2=input("enter string")
if sorted(s1)==sorted(s2):
    print(s1,"and",s2,"are anagram")
else:
    print("not anagram")