'''

3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
'''

import randomlist

from folders import create_dirs, remove_dirs

create_dirs()
remove_dirs()
print(randomlist.get_random_choise([1, 2, 3, 4, "Микола", "Петро"]))
print(randomlist.get_random_choise([]))