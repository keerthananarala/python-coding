a=input("enter string 1")
b=input("enter string 2")
a1="".join(i for i in a if i.isalnum())
b1="".join(i for i in b if i.isalnum())
a2=sorted(a)
b2=sorted(b)
if a2==b2:
    print("the given strings are anagrams")
else:
    print("the given strings are not anagrams")