'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return f"Получен результат деления {divider}/{denominator} = {divider / denominator}"
        except:
            return (f"Получен результат деления {divider}/{denominator}. Деление на ноль недопустимо")



print(DivisionByNull.divide_by_null(14, 0))
print(DivisionByNull.divide_by_null(0, 14))
print(DivisionByNull.divide_by_null(10, 2))
