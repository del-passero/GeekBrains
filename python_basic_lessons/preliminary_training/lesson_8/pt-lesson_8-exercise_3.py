'''
Практическое задание
3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого. ###
В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
Функция должна сама работать со словарями и изменять их значения.
'''

import random

player = {"name": input("Введите имя игрока: "),
          "health": random.randint(90, 110)}

enemy = {"name": input("Введите имя врага: "),
         "health": random.randint(90, 110)}

# print('Создан игрок: ', player)
# print('Создан враг: ', enemy)

def attack(attacker, defender):
    attacker['damage'] = random.randint(45, 55) #урон должен быть разным на каждом ходу
    print(f"У {defender['name']} сейчас {defender['health']} здоровья")
    defender['health'] = defender['health'] - attacker['damage']
    print(f"Атакует {attacker['name']} и наносит {attacker['damage']} урона")
    if defender['health'] <= 0:
        print(f"{defender['name']} умер. Победил {attacker['name']}!")
    else:
        print(f"Уровень здоровья игрока {defender['name']} теперь составляет {defender['health']}")

#attack(player, enemy)

i = 1
while player["health"] > 0 and enemy["health"] > 0:
    print(f"\n{i} ход!")
    if i % 2 != 0: # для того, чтобы поменять местами в вызываемой функции аргументы атакующего и защищающегося
        attack(player, enemy)
    else:
        attack(enemy, player)
    i += 1
