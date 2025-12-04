x = input("enter a string:")
k =""
for i in x:
    if i.islower():
       k=k+i.upper()
    else:
        k=k+i.lower()
print(k)
