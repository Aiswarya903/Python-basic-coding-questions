# non-optimized way
# lst =[1,2,3,2,4,3]
# lst1 = sorted({x for x in lst if lst.count(x) > 1})
# print(lst1)

# optimized way
nums =[1,2,3,2,4,3]
seen = set()
dupes = set()
for num in nums:
    if num in seen:
        dupes.add(num)
    else:
        seen.add(num)
print(list(dupes))