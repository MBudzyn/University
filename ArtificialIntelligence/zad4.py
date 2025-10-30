"bardzo intuicyjne rozwiązanie, które polega na przesuwaniu okna o długości D po tablicy bits"
"znajduje maksymalną liczbę jedynek w oknie"
"w tym oknie będzie najmniej zamian, które trzeba wykonać, aby uzyskać ciąg jedynkowy"
"zwraca D - max_ones * 2 + counter_all_ones ponieważ musimy zliczyć jedynki znajdujące się poza oknem"

def opt_dist(bits, D):

    n = len(bits)
    if D>n:
        return 0
    counter = 0
    counter_all_ones = 0
    max_ones = 0

    for i in range(D):
        if bits[i] == 1:
            counter += 1
            counter_all_ones += 1
            max_ones += 1

    for j in range(D, n):
        if bits[j - D] == 1:
            counter -= 1

        if bits[j] == 1:
            counter += 1
            counter_all_ones += 1

        if counter > max_ones:
            max_ones = counter

    return D - max_ones * 2 + counter_all_ones






# Przykładowe użycie funkcji opt_dist
bits = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
print(opt_dist(bits, 10))  # Output: 3
print(opt_dist(bits, 4))  # Output: 4
print(opt_dist(bits, 3))  # Output: 3
print(opt_dist(bits, 2))  # Output: 2
print(opt_dist(bits, 1))  # Output: 1
print(opt_dist(bits, 0))  # Output: 2