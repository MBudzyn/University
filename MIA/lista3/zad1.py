n,a,b,c = map(int,input().split(" "))
table_with_number_of_pices = [0] * (n + 1)
if a <= n:
    table_with_number_of_pices[a] = 1
if b <= n:
    table_with_number_of_pices[b] = 1
if c <= n:
    table_with_number_of_pices[c] = 1
for i in range(1, n + 1):
    condition = False
    if i - a >= 0 and i - b >= 0 and i - c >= 0 and a != b and b != c and c != a:
        table_with_number_of_pices[i] = max(table_with_number_of_pices[i - a], table_with_number_of_pices[i - b], table_with_number_of_pices[i - c])
        condition = True
    elif i - a >= 0 and i - b >= 0 and a != b:
        table_with_number_of_pices[i] = max(table_with_number_of_pices[i - a], table_with_number_of_pices[i - b])
        condition = True
    elif i - a >= 0 and i - c >= 0 and a != c:
        table_with_number_of_pices[i] = max(table_with_number_of_pices[i - a], table_with_number_of_pices[i - c])
        condition = True
    elif i - b >= 0 and i - c >= 0 and b != c:
        table_with_number_of_pices[i] = max(table_with_number_of_pices[i - b], table_with_number_of_pices[i - c])
        condition = True
    elif i - a >= 0:
        table_with_number_of_pices[i] = table_with_number_of_pices[i - a]
        condition = True
    elif i - b >= 0:
        table_with_number_of_pices[i] = table_with_number_of_pices[i - b]
        condition = True
    elif i - c >= 0:
        table_with_number_of_pices[i] = table_with_number_of_pices[i - c]
        condition = True

    if condition and table_with_number_of_pices[i] != 0:
        # if not ((i == a or i == b or i == c) and table_with_number_of_pices[i] == 1):
        table_with_number_of_pices[i] += 1


print(table_with_number_of_pices[n])


