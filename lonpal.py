lst = ["dood","malayalam","loooooooooooool","took"]
max = 0
for i in lst:
    if i.lower()[::-1]==i.lower():
        l = len(i)
        if l > max:
            max = l
print(max)

