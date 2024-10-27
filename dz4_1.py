# Задание 1. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.


def def_summa(n1: int, n2: int) -> int:
    print(n1 + n2)


def def_difference(n1: int, n2: int) -> int:
    print(n1 - n2)


def def_division(n1: int, n2: int) -> float:
    print(n1 / n2)


def def_multiplication(n1: int, n2: int) -> int:
    print(n1 * n2)


def is_digit(n: int) -> list:
    digit_list = []
    while n > 0:
        digit_list.append(n % 10)
        n //= 10
    return digit_list


def def_max(n: int) -> int:
    numbers_list = is_digit(n)
    max_d = numbers_list[0]
    for num in numbers_list[1:]:
        if num > max_d:
            max_d = num
    return max_d


def def_min(n: int) -> int:
    numbers_list = is_digit(n)
    min_d = numbers_list[0]
    for num in numbers_list[1:]:
        if num < min_d:
            min_d = num
    return min_d


def def_sum(n: int) -> int:
    numbers_list = is_digit(n)
    summa = 0
    for num in numbers_list:
        summa += num
    return summa


def def_continue() -> bool:
    string = input('продолжим: ДА - "Y" НЕТ - "N" ')
    if string == "Y":
        return True
    else:
        return False


# num1 = int(input("число №1: "))


while True:
    num1 = int(input("число №1: "))
    operator = input(
        'выберите действие: "+" "-" "*" "/" '
        'или операцию: максимальная цифра числа - "max"'
        'минимальная цифра числа - "min" '
        'сумма цифр числа - "sum" '
        'Выход - "exit" '
    )
    if operator == "+":
        num2 = int(input("число №2: "))
        def_summa(num1, num2)
        if def_continue() == False:
            break
    elif operator == "-":
        num2 = int(input("число №2: "))
        def_difference(num1, num2)
        if def_continue() == False:
            break
    elif operator == "/":
        num2 = int(input("число №2: "))
        def_division(num1, num2)
        if def_continue() == False:
            break
    elif operator == "*":
        num2 = int(input("число №2: "))
        def_multiplication(num1, num2)
        if def_continue() == False:
            break
    elif operator == "max":
        print(f"максимальная цифра = {def_max(num1)}")
        if def_continue() == False:
            break
    elif operator == "min":
        print(f"минимальная цифра = {def_min(num1)}")
        if def_continue() == False:
            break
    elif operator == "sum":
        print(f"сумма цифр числа {num1} = {def_sum(num1)}")
        if def_continue() == False:
            break
    elif operator == "exit":
        break
    else:
        print("неверная команда")
        break
