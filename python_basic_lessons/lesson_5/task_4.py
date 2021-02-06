"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
my_file = "for_task_4.txt"
new_file = "for_task_4_NEW.txt"
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_data = []

try:
    with open(my_file, 'r', encoding='utf-8') as my_file_obj:
        for i in my_file_obj:
            i = i.split(' ', 1)
            new_data.append(rus[i[0]] + ' ' + i[1])
    with open(new_file, 'w', encoding='utf-8') as new_file_obj:
        new_file_obj.writelines(new_data)
    with open(new_file, 'r', encoding='utf-8') as new_file_obj: # откроем посмотреть что получилось
        lines = new_file_obj.readlines()
        for line in lines:
            print(line.rstrip())
except IOError as e:
    print(e)
except (ValueError, IndexError):
    print("Некорректные данные")