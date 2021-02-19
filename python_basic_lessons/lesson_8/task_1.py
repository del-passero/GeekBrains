'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

from datetime import date

class Data: #инициализируем
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')] #преобразовываем в число
            return f"Проверим-ка мы получившиееся значения: \nчисло - {type(day), day}\nмесяц - {type(month), month}\nгод - {type(year), year}"
        except ValueError:
            return 'Введена некорректная дата!'

    @staticmethod
    def valid(data):
        try:  #валидируем
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Валидация прошла успешно. Дата указана корректно!'
        except ValueError:
            return 'Валидация не пройдена. Дата указана некорректно!'



print(Data.type('25-02'))
print(Data.type('19-02-2021'))
print(Data.type('19-feb-2021'))

print(Data.valid('19-02-2021'))
print(Data.valid('33-13-2023'))