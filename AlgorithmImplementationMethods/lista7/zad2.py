def fun():
    first_string = input()
    second_string = input()
    if second_string == "a":
        print(1)
    elif "a" in second_string:
        print(-1)
    else:
        print(2**len(first_string))

number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    fun()