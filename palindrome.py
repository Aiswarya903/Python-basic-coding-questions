x =101
p = 0
while x !=0:
    l = x%10
    p = p*10 + l
    x = x//10
print(p)
if p !=x:
    print("palindrome")
else:
    print(" not palindrome")