'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def div(*args):
    def enter_values(*args):
        try:
            dividend = int(input("Введите делимое число: "))
            divider = int(input("Введите делитель числа: "))
        except ValueError:
            return 'Вы ввели не число'
        return dividend, divider
    try:
        result = dividend / divider
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return result



div()