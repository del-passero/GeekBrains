'''
4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. 
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

def

    damage / armor
#attack(player, enemy)

i = 1
while player["health"] > 0 and enemy["health"] > 0:
    print(f"\n{i} ход!")
    if i % 2 != 0: # для того, чтобы поменять местами в вызываемой функции аргументы атакующего и защищающегося
        attack(player, enemy)
    else:
        attack(enemy, player)
    i += 1
