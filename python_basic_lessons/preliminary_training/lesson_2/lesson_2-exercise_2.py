'''
2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.
'''
exponentiation = 2 #переменная введена на тот случай, если возводить нужно будет не в степень 2
num = int(input("Введите число больше 0, но меньше 10: "))
while num < 0 or num > 10:
    print("Вы ввели число, находящееся вне заданного диапазона.")
    num = int(input("Введите число больше 0, но меньше 10: "))
if 0 < num < 10:
    num = num**exponentiation
    print(f"Если ваше число возвести в степень {exponentiation} получится {num}")


#и альтернативный вариант, который мне нравится меньше
'''
while True:
    exponentiation = 2  # переменная введена на тот случай, если возводить нужно будет не в степень 2
    num = int(input("Введите число больше 0, но меньше 10: "))
    if 0 < num < 10:
        num = num ** exponentiation
        print(f"Если ваше число возвести в степень {exponentiation} получится {num}")
        break
    else:
        print("Вы ввели число, находящееся вне заданного диапазона.")
'''