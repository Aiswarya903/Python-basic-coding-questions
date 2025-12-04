def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
x = int(input("enter a number"))
for i in range(x):
    print(fib(i))