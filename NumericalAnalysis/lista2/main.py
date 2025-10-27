from math import *

def zad1(x):
    print(1/(pow(x,3) + sqrt(pow(x,6) + pow(2023,2))))
def zad1lepiej(x):
    print(sqrt((pow(x,6)/pow(2023,2))/2023) - pow(x,3)/pow(2023,2))
def zad2(x):
    print(log2(x) - 2)
def zad2lepiej(x):
    print(log2(x/4))

zad2(4.000000000000005)
zad2lepiej(4.000000000000005)

def pierwiastki_kwadratowego(a,b,c):
    if b < 0:
        pierwiastek1 = -b + sqrt(b**2 - 4*a*c)
        pierwiastek2 = c/a*pierwiastek1
        return pierwiastek1,pierwiastek2
    else:
        pierwiastek1 = -b - sqrt(b ** 2 - 4 * a * c)
        pierwiastek2 = c / a * pierwiastek1
        return pierwiastek1, pierwiastek2

def pierwiastki_kwadratowe_zle(a,b,c):
    return -b + sqrt(b**2 - 4*a*c), -b - sqrt(b ** 2 - 4 * a * c)
print(pierwiastki_kwadratowe_zle(1,10000000000000000,1))
print(pierwiastki_kwadratowego(1,10000000000000000,1))