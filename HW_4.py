# Предусловие.
# Задачи 3 и 4 выполнить в 2-х вариантах:
# 1) В процедурном виде (весь код в одной процедуре).
# 2) В виде функций - код разбит на функции. Отдельные функции можно вынести в другие .py файлы и вызывать их в main.py
# предварительно импортируя в main.py.
#
#
# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определить самому.
#
# quantity_money = int(input("Введи сумму в грн. "))
# print(f"Ты ввёл {quantity_money} грн.")
# print(f"Конвертированная сумма в USD = {round(quantity_money/36.96, 2)}$")
#
# -----------------------------------------------------------------------------------------------------------------------
#
#
# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в  = int"
#     3. Валюту пользователя определите сами.
#
# quantity_money = int(input("Введи сумму в грн. "))
# print(f"Ты ввёл {quantity_money} грн.")
# print(f"Конвертированная сумма в USD = {round(quantity_money/36.96, 2)}$")
# print(f"Конвертированная сумма в EUR = {round(quantity_money/40.24, 2)}€")
# print(f"Конвертированная сумма в CHF = {round(quantity_money/41.13, 2)}₣")
# print(f"Конвертированная сумма в GBP = {round(quantity_money/46.96, 2)}£")
# print(f"Конвертированная сумма в CNY = {round(quantity_money/5.10, 2)}元")
#
# -----------------------------------------------------------------------------------------------------------------------
#
#
# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.
#
# method 1
# quantity_money = input("Введи сумму в грн. ")
# if quantity_money == '':
#     print("Вы ввели пустое поле. Введите число.")
# elif quantity_money[0] == '-':
#     print("Введите положительное число.")
# elif not quantity_money.isdigit():
#     print("Вы ввели не число. Введите число.")
# else:
#     print(f"Ты ввёл {quantity_money} грн.")
#     print(f"Конвертированная сумма в USD = {round(int(quantity_money) / 36.96, 2)}$")
#     print(f"Конвертированная сумма в EUR = {round(int(quantity_money) / 40.24, 2)}€")
#     print(f"Конвертированная сумма в CHF = {round(int(quantity_money) / 41.13, 2)}₣")
#     print(f"Конвертированная сумма в GBP = {round(int(quantity_money) / 46.96, 2)}£")
#     print(f"Конвертированная сумма в CNY = {round(int(quantity_money) / 5.10, 2)}元")
#
# method 2
# def currency_disp(inp):
#     print(f"Ты ввёл {inp} грн.")
#     print(f"Конвертированная сумма в USD = {round(int(inp) / 36.96, 2)}$")
#     print(f"Конвертированная сумма в EUR = {round(int(inp) / 40.24, 2)}€")
#     print(f"Конвертированная сумма в CHF = {round(int(inp) / 41.13, 2)}₣")
#     print(f"Конвертированная сумма в GBP = {round(int(inp) / 46.96, 2)}£")
#     print(f"Конвертированная сумма в CNY = {round(int(inp) / 5.10, 2)}元")
#
# def validation(inp):
#     if inp == '':
#         print("Вы ввели пустое поле. Введите число.")
#     elif inp[0] == '-':
#         print("Введите положительное число.")
#     elif not inp.isdigit():
#         print("Вы ввели не число. Введите число.")
#     else:
#         return currency_disp(inp)
#
# validation(input("Введи сумму в грн. "))
#
# -----------------------------------------------------------------------------------------------------------------------
#
#
# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.
#
# method 1
#
# while True:
#     curr = input("Выберите валюту из: 'USD','EUR','CHF','GBP','CNY' ")
#     value = input("Введите сумму ")
#
#     if value == '':
#         print("Вы ввели пустое поле. Введите число.")
#     elif value[0] == '-':
#         print("Введите положительное число.")
#     elif not value.isdigit():
#         print("Вы ввели не число. Введите число.")
#
#     elif curr == "USD":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 36.96, 2)}$")
#     elif curr == "EUR":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 40.24, 2)}€")
#     elif curr == "CHF":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 41.13, 2)}₣")
#     elif curr == "GBP":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 46.96, 2)}£")
#     elif curr == "CNY":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 5.10, 2)}元")
#
#
# method 2
#
# def cur_disp(curr, value):
#     if curr == "USD":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 36.96, 2)}$")
#     elif curr == "EUR":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 40.24, 2)}€")
#     elif curr == "CHF":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 41.13, 2)}₣")
#     elif curr == "GBP":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 46.96, 2)}£")
#     elif curr == "CNY":
#         print(f"Вы ввели сумму {value} и валюту {curr}")
#         print(f"Конвертированная сумма в {curr} = {round(int(value) / 5.10, 2)}元")
#
# def validation(value):
#     if value == '':
#         print("Вы ввели пустое поле. Введите число.")
#     elif value[0] == '-':
#         print("Введите положительное число.")
#     elif not value.isdigit():
#         print("Вы ввели не число. Введите число.")
#     else:
#         cur_disp(curr, value)
#
# while True:
#     curr = input("Выберите валюту из: 'USD','EUR','CHF','GBP','CNY' ")
#     value = input("Введите сумму ")
#     validation(value)

















