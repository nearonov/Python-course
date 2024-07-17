# for n in range (0,8,2):
#     print(1)

# my_frutis = ['apple', 'lime', 'banan']
# for i in my_frutis:
#     print(i, end=' ')

# my_dict = {'apple': 1, 'lime': 2, 'banan': 3}
# for i in my_dict:
#     print(i, my_dict[i], end='   ')

# my_dict = {'apple': 1, 'lime': 2, 'banan': 3}
# for key, valu in my_dict.items():
#     #key, valu = i
#     print(key, valu, end='  ')

# my_set = {1, 4, 'abc', "Eugene"}
# for i in my_set:
#     print(i, end=' ')

# my_dict = {'apple': 1, 'lime': 2, 'banan': 3}
# list = []
# for key in my_dict.items():
#     #key, valu = i
#     list.append(key)
# print(list)

# -------------------------------------------
# Завдання #1
# 1. функц.конвертує словник в список кортежів (key,value)
# 2. якщо значення ключа ціле число , то його помножим на 2 перед
# додаванням в кортеж.
# -------------------------------------------

# def dict_to_list(arg):
#     other_dict = {}
#     for key,value in arg.items():
#          if type(value) == int:
#              value*=2
#              other_dict[key]=value
#          # else:
#          #     value=value
#          #     other_dict[key]=value
#     #print(other_dict)
#     list = []
#     for key in other_dict.items():
#         list.append(key)
#     return list
#
#
# my_dict = {'apple': 1, 'lime': 2, 'banan': '3'}
# print(dict_to_list(my_dict))


# || СПОСІБ

# def dict_to_list(arg):
#     my_list = []
#     for key, value in arg.items():
#         if type(value) == int:
#             value *= 2
#             my_list.append((key, value))
#     return my_list
#
#
# my_dict = {'apple': 1, 'lime': 2, 'banan': '3'}
# print(dict_to_list(my_dict))
# -------------------------------------------
# Завдання #2
# 1. Функція яка буде фільтр. список.
# 2. Функція має два параметра (список і тип значення).
# 3. Функція повинна повернутии список в якому залишутся тільки
# тільки значення того типу котрий був переданий в виклику функц.
# другим аргументом .
# -------------------------------------------

# def filter_list(my_list,my_type):
#     other_list = []
#     for i in my_list:
#         if type(i) == type(my_type):
#             other_list.append(i)
#     return other_list
#
# good_list = ['Euvgene',True,23,123,(45,67)]
# value = False
# print(filter_list(good_list,value))

# || СПОСІБ
# def filter_list(my_list,my_type):
#     # def check_to_list(elem):
#     #     return isinstance(elem,my_type)
#     # return list(filter(check_to_list,my_list))
#     return list(filter(lambda elem:type(elem) is my_type, my_list))
#
# good_list = ['Euvgene',True,23,123,(45,67)]
# value = int
# print(filter_list(good_list,value))

# -------------------------------------------
# скорочений for in
# -------------------------------------------

# my_list = [2, -5, -23, -67, -56]
# abs_list = [abs(num) for num in my_list if num %2==0]
# print(abs_list)
# [2, 56]


# my_set = {2, 5, 9}
# other_set = {val*val for val in my_set}
# print(other_set)
# {81, 4, 25}

# my_scores = {'a': 10, 'b': 3, 'c': 34}
# scores = {key: valu * 10 for key, valu in my_scores.items()}
# print(scores)
# {'a': 100, 'b': 30, 'c': 340}

# І з списка робим словник

# my_scores = [10, 7, 12]
# scores = {key:valu for key, valu in enumerate(my_scores)}
# print(scores)


# -------------------------------------------
# Завдання №1
# 1. Створити словник значення кючів тип str.
# 2. Створити новий слов.на основі існуючого , в якому всі значення ключів
# будуть в верхньому регістрі.
# -------------------------------------------

# my_dict = {23:'qwe', 4:'asd', 78:'zxc'}
# other_dict = {key: valu.upper() for key, valu in my_dict.items()}
# print(other_dict)
# {23: 'QWE', 4: 'ASD', 78: 'ZXC'}

# || спосіб:

# my_dict = {23:'qwe', 4:'asd', 78:'zxc'}
# other_dict = {}
# for key ,valu in my_dict.items():
#         other_dict[key]=valu.upper()
# print(other_dict)
# {23: 'QWE', 4: 'ASD', 78: 'ZXC'}

# -------------------------------------------
# Завдання №2
# 1.Создати список з елементами типа str.
# 2. З цього списку зробіть новий список в якому залишится
# тільки строки довжина яких більше трьох.
# -------------------------------------------

# my_list = ['qw', 'Eugene', 'a', 'Nearonov']
# info = [i for i in my_list if len(i)>3]
# print(info)
# ['Eugene', 'Nearonov']


#-------------------------------------------
# Генератор в скороченом for in
# Він має дуже маленький розмір і потім в любому місці можно провести ітарацію.
#-------------------------------------------
# from sys import getsizeof
# nums = (3, 56, 7)
# squares = (num * num for num in nums)# генератор
# print(squares)
# # generator object
# print(getsizeof(squares))
# # 208
#
# for i in squares:
#     print(i,end=' ')
# 9 3136 49


from sys import getsizeof

squares_get=(num *num for num in range(10000))
squares=[num *num for num in range(10000)]
print(getsizeof(squares_get),'<', getsizeof(squares))
# 208 < 85176

for elem in squares_get:
    print(elem,end=' ')
    if elem==100:
            break
print('- Етарація генератора')