'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = True if is_police else False

    def go(self):
        if self.is_police: # ну не зря ж мы вводим это свойство
            return f'Ваш крутой полицейский {self.name} с цветом "{self.color}" поехал.'
        else:
            return f'Ваш {self.name} с цветом "{self.color}" поехал.'

    def stop(self):
        return f'\nВаш {self.name} остановился.'

    def turn(self, direction):
        return f'\nВаш {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed} км\ч'

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили допустимые 60 км\ч, ваша скорость составляет {self.speed} км\ч'
        else:
            return f'\nВаша скорость {self.speed} км\ч'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили допустимые 40 км\ч, ваша скорость составляет {self.speed} км\ч'
        else:
            return f'\nВаша скорость {self.speed} км\ч'

town = TownCar('Hyundai Solaris', 80, 'белый')
print('\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('DeLorean DMC-12', 142, 'серебряный')
print('\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('КамАЗ', 50, 'оранжевый')
print('\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('УАЗ-452Д', 100, 'синий', True)
print('\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())