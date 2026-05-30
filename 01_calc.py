first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
operation = input("Введыть операцію (+, -, *, /): ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number == 0:
        print("Діленя на 0 неможливе!")
    else:
        print(first_number / second_number)
else:
    print("Неіснуяча операція!")
