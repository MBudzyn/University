def zad5(x,a,iteracje):
    if iteracje <=0:
        return x
    else:
        return zad5(2 * x - a * x**2 ,a,iteracje -1)



for i in range(25):
    if zad5(0.05, 9, i) == 1/9:
        print(i)
        break
for i in range(25):
    if zad5(0.0001, 20, i) == 1/20:
        print(i)
        break
for i in range(25):
    if zad5(0.00001, 100, i) == 1/100:
        print(i)
        break
for i in range(25):
    if zad5(0.4, 2, i) == 1/2:
        print(i)
        break
for i in range(25):
    if zad5(0.1, 9, i) == 1/9:
        print(i)
        break
for i in range(100):
    if zad5(0.0000000005, 1000, i) == 1/1000:
        print(i)
        break
for i in range(100):
    if zad5(0.00005, 9, i) == 1/9:
        print(i)
        break
for i in range(100):
    if zad5(0.00000005, 9, i) == 1/9:
        print(i)
        break

