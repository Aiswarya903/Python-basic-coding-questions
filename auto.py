x = int(input("enter a number"))
a = x*x
len=len(str(x))
if a%(10**len)==x:
    print("num is automorphic")
else:
    print("num is not automorphic")