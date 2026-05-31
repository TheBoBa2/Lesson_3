input_nums = list(map(int, input("Введіть числа: ").split()))
if len(input_nums) > 1:
    last_element = input_nums.pop()
    input_nums.insert(0, last_element)
else:
    print("недостятня кількість елементів для змін")
print("ітоговий список: ", input_nums)
