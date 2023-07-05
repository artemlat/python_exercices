# #1. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
# l = [1, 2, 3]
# a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']

#metod 1
# l = [1, 2, 3]
# a = 'abc'
# result = l
# result.extend(a)
# print(result)

#method 2
# l = [1, 2, 3]
# a = 'abc'
# result = l
# for i in a:
#     result.append(i)
# print(result)
#-------------------------------------------------------------------------------------------


# 2. Все чётные числа вывести в другой список
# l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
# k = []
# for i in l:
#     if i % 2 == 0:
#         k.append(i)
# print(k)
#-------------------------------------------------------------------------------------------


# 3. Все emails у которых есть слово test вывести в другой список
# l = ['webtest1@gmail.com',
#      'alex_dr5@gmail.com',
#      'elena_viktorovna@gmail.com',
#      'infotest@gmail.com',
#      'sigmatesst@gmail.com',
#      'planet.dollsatest@gmail.com',
#      'loadtestsinfo@gmail.com',
#      'straightwaytest@gmail.com',
#      'test.of.tests@gmail.com',
#      'bigmac@gmail.com',
#      'bigmactest@gmail.com',
#      'kfc_test_supply@gmail.com',
#      'cyberdesk@gmail.com',
#      'supportonlinetest@gmail.com'
#      ]
# k = list()
# for i in l:
#     if "test" in i:
#         k.append(i)
# print(k)
#-------------------------------------------------------------------------------------------


# 4. Найти самое маленькое число в списке
# l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]
# min = l[0]
# for i in l:
#     if i < min:
#         min = i
# print(min)
#-------------------------------------------------------------------------------------------


# 5. Сравнить 2 строки без учёта регистра
# str_1 = input().lower()
# str_2 = input().lower()
#
# if str_1 == str_2:
#     print("Строки одинаковые")
# else:
#     print("Строки разные")
#-------------------------------------------------------------------------------------------


# 6. Проверить является ли массив подмножеством другого массива
# l1 = [1,4,6]
# l2 = [9,5,1,10,4,33,2,6,0,8]
#-------------------------------------------------------------------------------------------


# 7. Проверить является ли массив подмножеством другого массива
# l1 = [1,4,6]
# l2 = [9,5,1,10,4,33,2,6,0,8]
#
# for i in l1:
#     if i not in l2:
#         print(False)
#         break
# else:
#     print(True)
#-------------------------------------------------------------------------------------------


# 8. Напишите функцию, которая принимает строку и
# возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.

# def letters_count(inp):
#     inp = inp.lower()
#     count = 0
#     sp = []
#     for i in inp:
#         if i in 'abcdefghijklmnopqrstuvwxyz' and inp.count(i) > 1 and i not in sp:
#             print(f"Количество букв {i} в слове {inp} - {inp.count(i)}")
#             sp.append(i)
#
# letters_count(input())

#-------------------------------------------------------------------------------------------


# 9. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.

# no_duplicate_letters("Здравствуйте, Александра") ➞ False
# Две в в «Здравствуйте», три a в «Александра».

# no_duplicate_letters("Всегда дожимай до конца") ➞ True

# def no_duplicate_letters(inp):
#     sp = inp.split(' ')
#     for i in sp:
#         mas = []
#         for j in i:
#             if j not in mas:
#                 mas.append(j)
#             else:
#                 return(False)
#     else:
#         return(True)
# print(no_duplicate_letters(input()))
#-------------------------------------------------------------------------------------------


#10. Напишите функцию, которая проверяет сложность пароля. Функция проверяет ряд условий и оценивает сложность пароля.
# За каждое выполненое условие пароль получает бал.
#
# Если выполняется одно условие - функция возвращает 1, если выполненяется 5 условий - функция вернет 5.
#
# Условия которые нужно проверить:
#
# длина пароля не меньше 6 символов,
# пароль содержит хотя бы 1 цифру,
# пароль содержит хотя бы одну заглавную букву,
# пароль содержит хотя бы одну строчную букву,
# пароль содержит хотя бы один из специальных символов: !@#$%^&*()-+
#
# Типы символов, которые будут содержаться в пароле во время тестирования:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
# Пароль не должен содержать кириллических символов


# def password_rate(inp):
#     for i in inp.lower():
#         if i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
#             return "Пароль содержит недопустимые символы"
#     rate = 0
#     if len(inp) >= 6:
#         rate += 1
#     for i in inp:
#         if i.isdigit():
#             rate += 1
#             break
#     for i in inp:
#         if i.isupper():
#             rate += 1
#             break
#     for i in inp:
#         if i.islower():
#             rate += 1
#             break
#     for i in inp:
#         if i in "!@#$%^&*()-+":
#             rate += 1
#             break
#     return f"Cложность пароля {rate}"
#
# print(password_rate(input()))
