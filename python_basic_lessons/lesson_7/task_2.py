"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod, abstractproperty

class Сlothes(ABC):
    #Класс абстрактной одежды
    @property
    @abstractmethod
    # Абстрактный метод для проведения расчётов (позжже ммы его переопределим)
    def textile_count(self):
        pass

    @property
    @abstractmethod
    #Абстрактное свойство "Имя
    def name(self):
        pass

    def __str__(self):
        # функция для отображения объекта в строке
        return f"На {self.name} потребуется {round(self.textile_count, 2)} погонных метров ткани"

    def __repr__(self):
         # функция для отображения  в строках при вложенных вызовах
        return self.__str__()

class Coat(Сlothes):
    def __init__(self, volume: float):
        self._volume = volume

    @property
    def textile_count(self):
        return self._volume / 6.5 + .5

    @property
    def name(self):
        return "Пальто"

class Suit(Сlothes):
    def __init__(self, height: float):
        self._height = height

    @property
    def textile_count(self):
        return self._height * 2 + .3

    @property
    def name(self):
        return "Костюм"


all_clothes = [Coat(52), Suit(1.76)]

print(*all_clothes, sep="\r\n") #распаковываем список
print("Всего потребуется: " + str(round(sum([x.textile_count for x in all_clothes]), 2)) + " погонных метров ткани")

