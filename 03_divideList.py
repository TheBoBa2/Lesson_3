input_lst = list(map(int, input("Введіть числа: ").split()))

lst_mid = (len(input_lst) + 1) // 2

if len(input_lst) > 0:
    print([input_lst[:lst_mid], input_lst[lst_mid:]])
else:
    print([[], []])
