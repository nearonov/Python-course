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


