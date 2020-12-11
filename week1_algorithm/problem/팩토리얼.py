def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

n = int(input())
if n == 0:
    print(1)
else:
    print(factorial(n))