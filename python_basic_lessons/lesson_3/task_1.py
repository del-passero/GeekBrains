'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def div(a, b):
    try:
        a = int(input("Введите делимое: "))
        b = int(input("Введите делитель: "))
        result = a / b
    except ValueError:
        return 'Не получилось! Вы ввели не число!'
    except ZeroDivisionError:
        return "Не получилось! На ноль делить нельзя!"
    return result
a = 0
b = 0
question = None
while question != "00":
    result = print(f'Ваш результат: {div(a, b)}')
    question = input("\n Хотите продолжить? Если да - нажмите Enter, если нет - введите '00' и программа закроется.")
print("До свидания!")