
def has_intiger_square(number):
    t = number**(1/2)
    if int(t) == t:
        return t
    return False
def is_prime(number):
    if number == 1:
        return False
    for i in range(2,int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True
def is_T_prime(number):
    square = has_intiger_square(number)
    if square:
        if table_with_prime[int(square)]:
            return True
    return False

def sito_arytostenesa(number):
    table = [True for i in range(number + 1)]
    for i in range(2,int(number**(1/2)) + 1):
        if table[i]:
            for j in range(i*i,number + 1,i):
                table[j] = False
    table[0] = False
    table[1] = False
    return table
number_of_data = int(input())
table_with_data = list(map(int,input().split()))
table_with_prime = sito_arytostenesa(1000001)
for i in table_with_data:
    if is_T_prime(i):
        print("YES")
    else:
        print("NO")


