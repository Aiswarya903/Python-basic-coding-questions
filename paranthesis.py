st = "({[]})"
stack = []
mapping = {")":"(","]": "[", "}" : "{"}
flag = 0
for i in st:
    if i in "{[(":
        stack.append(i)
    else:
        if not stack or mapping[i] != stack[-1]:
            print("invalid")
            flag = 1
            break
        stack.pop()
if flag == 0:
    print("valid")
else:
    print("invalid")
