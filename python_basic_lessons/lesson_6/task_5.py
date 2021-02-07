'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title: str
    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    title = "Ручкой"
    def draw(self):
        print(f"{self.title} пишут!")

class Pencil(Stationery):
    title = "Карандашом"
    def draw(self):
        print(f"{self.title} чертят!")

class Handle(Stationery):
    title = "Маркером"
    def draw(self):
        print(f"{self.title} рисуют!")

stationery = Stationery()
stationery.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()




