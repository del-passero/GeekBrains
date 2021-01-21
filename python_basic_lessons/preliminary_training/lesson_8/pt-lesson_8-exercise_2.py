'''
Практическое задание
2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
'''

def max_num(first, second, third):
    return max(first, second, third)
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

print("Максимальное число из введенных:", max_num(first, second, third))


