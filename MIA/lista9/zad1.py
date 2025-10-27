number_of_data = int(input())
table_with_data = list(map(int,input().split()))
result = False
for index in range(number_of_data):
    all_results = set()
    all_results.add(table_with_data[table_with_data[table_with_data[index] - 1] - 1])
    all_results.add(table_with_data[table_with_data[index] - 1])
    all_results.add(table_with_data[index])
    all_results = list(all_results)
    if index + 1 == table_with_data[table_with_data[table_with_data[index]-1] -1] and len(all_results) == 3:
        result = True
if result:
    print("YES")
else:
    print("NO")
