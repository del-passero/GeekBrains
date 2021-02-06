"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_file = "for_task_3.txt"
count = 0 # счетчик для цикла когда будем количество сотрудников считать
sum_for_average = 0 # переменнаая для вычисления средней зарплаты

try:  # а вдруг файл удалится
    with open(my_file, 'r', encoding='utf-8') as my_file_obj:
        staff = {}
        for line in my_file_obj:
            surname, salary = line.split()
            staff[surname] = salary
            count += 1
            sum_for_average += int(salary)
            if int(salary) < 20000:
                print(f'У сотрудника: {surname} - оклад меньше 20000.0, а если быть более точным, то {salary} руб.')
        print(f'Всего работают {count} сотрудников, и средняя величина дохода у них - {sum_for_average / count} руб.')
except IOError as e:
    print(e)