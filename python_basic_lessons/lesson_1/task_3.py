'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
n = input("Введите число n - ")
print(len(n))
while not n.isdigit() and len(n) != 1:
    n = input("Введите число n - ")

amount = (int(n) + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print(f"Сумма чисел n + nn + nnn составляет {amount}")
