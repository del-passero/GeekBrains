"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_file = "for_task_5.txt"
values = "3 14 15 7 40"
my_sum = 0

try:
    with open(my_file, 'w', encoding='utf-8') as my_file_obj:
        my_file_obj.write(values)
    with open(my_file, 'r', encoding='utf-8') as my_file_obj:
        data = my_file_obj.read()
    for value in data.split():
        my_sum += int(value)
except IOError as e:
    print(e)
except ValueError:
    print("Некорректные данные")

print(f"Сумма чисел в файле: {my_sum}")
