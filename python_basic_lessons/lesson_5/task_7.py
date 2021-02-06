"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
my_file = 'for_task_7.txt'
my_json_file = 'for_task_7.json'
profit = {}
profit_for_dict = {}
total_profit  = 0 # для промежуточного расчета общей прибыли
average_profit = 0
i = 0 # счетчик для будущего определения безубыточных фирм
try:
    with open(my_file, 'r', encoding='utf-8') as my_file_obj:
        for line in my_file_obj:
            name, form_of_ownership, revenue, costs = line.split()
            profit[name] = int(revenue) - int(costs)
            if profit.setdefault(name) >= 0:
                total_profit = total_profit + profit.setdefault(name)
                i += 1
        if i != 0:
            average_profit = total_profit / i
            print(f'Средняя прибыль по безубыточным компаниям - {average_profit:.2f}')
        else:
            print(f'Все компании работают в убыток')
        profit_for_dict = {'Cредняя прибыль': round(average_profit)}
        profit.update(profit_for_dict)
        print(f'Прибыль\убыток по компаниям - {profit}')

    with open(my_json_file, 'w', encoding='utf-8') as my_json_obj:
        json.dump(profit, my_json_obj)
        js_str = json.dumps(profit)
except IOError as e:
    print(e)
except ValueError:
    print("Некорректные данные")
print(f'Создан файл с расширением json со следующим содержимым:\n{js_str}')

