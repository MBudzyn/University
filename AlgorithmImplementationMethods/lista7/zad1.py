def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = int(input())
print((x * (x-1) * (x-2) * (x-3) * (x-4))**2 // 120)


