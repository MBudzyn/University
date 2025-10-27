
def pierwiastek(x,a,iteracje):
    # a = m * 2**c
    if iteracje <=0:
        return x
    else:
        return pierwiastek(0.5 * (a/x + x),a,iteracje -1)

def zad7(m,c):
    if c%2 == 0:
        return [pierwiastek(1,m,10),m/2]
    else:
        return [pierwiastek(1,2*m,10),m//2]

for i in range(-100,0):
    if pierwiastek(1/i, 9, 20) == 3:
        print(f"zbiezna -1/{i}")

for i in range(1,100):
    if pierwiastek(1/i, 9, 20) == 3:
        print(f"zbiezna 1/{i}")

for i in range(-100,0):
    if pierwiastek(i, 9, 20) == 3:
        print(f"zbiezna -{i}")

for i in range(1,100):
    if pierwiastek(i, 9, 20) == 3:
        print(f"zbiezna {i}")

for i in range(100,10000):
    if pierwiastek(i, 9, 20) == 3:
        print(f"zbiezna {i}")

#zbiezne dla x0 >0
