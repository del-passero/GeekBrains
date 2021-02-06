"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = "for_task_2.txt"
line_num = 0 #для красивого вывода

try:  # а вдруг файл удалится
    with open(my_file, encoding='utf-8') as my_file_obj:
        lines = [line for line in my_file_obj.readlines() if line != '\n']
except IOError as e:
    print(e)
print(f"В файле содержится {len(lines)} непустых строк:")
for line in lines:
    # пока сам не забыл .rstrip() возвращает копию строки, в которой из конца строки все символы были вырезаны (в нашем случае '\n')
    # применил я это для "красивого" вывода
    line_num += 1 #пришлось делать такой костыль, потому что я учитываю только непустые строки
    print(f'В строке №{line_num}: "{line.rstrip()}" содержится {len(line.split())} слов')

