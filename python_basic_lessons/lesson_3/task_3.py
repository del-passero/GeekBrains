'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''

def my_func(a, b, c):
    try:
        my_list = [a, b, c]
        my_list.remove(min(a, b, c))
        return sum(my_list)
    except NameError:
        print(f'Что-то пошло не так!')


#экспериментирую с try\except
try:
    a = int(input("Введите первое число: "))
except ValueError:
    a = 0
    print('Вы ввели не число! Оно не будет учитываться при суммировании')

try:
    b = int(input("Введите второе число: "))
except ValueError:
    b = 0
    print('Вы ввели не число! Оно не будет учитываться при суммировании')
try:
    c = int(input("Введите третье число: "))
except ValueError:
    c = 0
    print('Вы ввели не число! Оно не будет учитываться при суммировании')


print(f'Ваш результат {my_func(a, b, c)}')
