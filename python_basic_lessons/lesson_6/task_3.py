'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)} # не будем заморачиваться с float

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_person_position(self):
        return f"работает на должности {self.position}"

    def get_total_income(self):
        return f'и зарабатывает {self._income["wage"] + self._income["bonus"]}'


p1 = Position('Анатолий', 'Чубайс', 'CEO', '1000000000', '400000000')
p2 = Position('Николай', 'Никончук', 'старший помощник младшего дворника', '11000', '2000')
print(p1.get_full_name(), p1.get_person_position(), p1.get_total_income())
print(p2.get_full_name(), p2.get_person_position(), p2.get_total_income())
