def zad6(x,a,iteracje):
    if iteracje <=0:
        return x
    else:
        return zad6(0.5 * x * (3 - a * x**2),a,iteracje -1)

print("x0 = 0.001")
for i in range(21):
    print(zad6(0.001, 9, i))
print("x0 = 2")
for i in range(4):
    print(zad6(2,9,i))
print("x0 = 0.01")
for i in range(15):
    print(zad6(0.01, 9, i))
print("x0 = 0.01")
for i in range(9):
    print(zad6(0.1, 9, i))

print("x0 = 0.4")
for i in range(6):
    print(zad6(0.4, 9, i))
print("x0 = 0.5")
for i in range(6):
    print(zad6(0.5, 9, i))
print("x0 = 0.3")
for i in range(5):
    print(zad6(0.3, 9, i))
print("x0 = 0.7")
for i in range(10):
    print(zad6(0.7, 9, i))




