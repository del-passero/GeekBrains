'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''

# было бы замечательно, если бы на разборе ДЗ показали как написать подобную программу без использования break
# вероятно я снова злоупотребил break и сontinue, но как сделать без них (с учетом желетельности ввода Enter польховталем) не очень представляю

goods = []
dict_frame = {'Наименование': '', 'Стоимость': '', 'Кол-во': '', 'Ед. изм.': ''}
#dict_analytics = {'Наименование': [], 'Стоимость': [], 'Кол-во': [], 'Ед. изм.': []} #если  нужны будут все значения.
dict_analytics = {'Наименование': set(), 'Стоимость': set(), 'Кол-во': set(), 'Ед. изм.': set()} #если нужны будут только уникальные значения.
num = 0
dict_option = None # непосредствнно для ввода значений
answer = None # для диалога с пользователем (чтобы он мог выйти в любой момент или провести аналитику)
permit_answer_values = ["Q", "Й", "A", "Ф", "F", "А"]  # список допустимых значений с учетом возможной неправильной раскладки

while True:
    answer = input("\nДля ввода значений нажмите 'Enter', для проведения аналитики нажите 'A'(Analytics). Для выхода из программы нажмите 'Q' (Quite): ")
    if answer.upper() not in permit_answer_values and answer != '':
        print("Прочитайте внимательно!!!")
        continue
    if answer.upper() == 'Q' or answer.upper() == 'Й':
        print("До свидания!")
        break
    num += 1
    if answer.upper() == 'A' or answer.upper() == 'Ф' or answer.upper() == 'F' or answer.upper() == 'А':
        print(f'\nВаши данные проанализированы:')
        for key, value in dict_analytics.items():
            print(f'{key[:]}: {value}')
        continue # чтобы была возможность выйти из цикла не вводя заново
    for f in dict_frame.keys():
        dict_option = input(f'Введите "{f}": ') # тут конечно можно было бы еще для цены и количества ввести доп. проверку на корректность ввода,но в условии такого нет
        dict_frame[f] = dict_option
        dict_analytics[f].add(dict_frame[f])
    goods.append((num, dict_frame))


#        if (f == 'price' or f == 'quantity') потом допилить проверку количества и цены