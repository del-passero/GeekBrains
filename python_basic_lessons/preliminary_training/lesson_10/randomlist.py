'''
2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
'''

import random as rd

def get_random_choise(input_list):
    if input_list:
        result = rd.choice(input_list)
        return result
if __name__ == '__main__':
    print(get_random_choise([1, 2, 3, 4, "Микола", "Петро"]))
    print(get_random_choise([]))