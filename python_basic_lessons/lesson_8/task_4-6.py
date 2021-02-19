'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class Warehouse:
    def __init__(self):
        self._dict = {} # иницициализируем словарь для хранения

    def add_to(self, equipment):# в словарь обьект по его названию, в значении - список экземпляров этого оборудования
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name): # извлекаем из значения обьект по названию группы. Дальше можно расширить поиск по серии, марки и т.д.
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

class Equipment:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, year):
        super().__init__(name, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.year}'

    def action(self): # уникальный метод для класса
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)

    def action(self): # уникальный метод для класса
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)

    def action(self): # уникальный метод для класса
        return 'Копирует'


Warehouse = Warehouse()
# создаем объект и добавляем
scaner = Scaner('Sony', 2018)
Warehouse.add_to(scaner)
xerox = Xerox('Хризантема', 2021)
Warehouse.add_to(xerox)
printer = Printer('PPT-14', 'Печатник', 2020)
Warehouse.add_to(printer)
# выводим склад
print(Warehouse._dict)
# забираем с склада и выводим склад
Warehouse.extract('Scaner')
print()
print(Warehouse._dict)