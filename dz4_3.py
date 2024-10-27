"""Задача 3. Число наоборот
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
каждое число на число, которое получается из исходного записью его цифр в
обратном порядке, затем складывает их, снова переворачивает и выводит
ответ на экран.
Пример:
Введите первое число: 102
Введите второе число: 123
Первое число наоборот: 201
Второе число наоборот: 321
Сумма: 522
Сумма наоборот: 225"""


def revers_num(n: int):
    r = 0
    while n > 0:
        r += n % 10
        n //= 10
        if n != 0:
            r *= 10
    return r


num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))
rev_num1 = revers_num(num1)
rev_num2 = revers_num(num2)
print(f"перевернутое число 1 = {rev_num1} \nперевернутое число 2 = {rev_num2}")

summa = rev_num1 + rev_num2
print(f"сумма перевернутых чисел = {summa}")
print(f"перевернутая сумма = {revers_num(summa)}")
