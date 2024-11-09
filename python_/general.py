import emoji
import asyncio
import itertools

# bd = open("D:\каб.УАРНЕТ.txt", 'r').read()
# ad = bd.split('\n')
# for i in ad:
#     print(i)  # список зі строк

# class Car:
#     brand = 'Mersedes'
#     color = 'black'
#
#     def __str__(self):
#         return f"Car obj \nbrand: {self.brand}\ncolor: {self.color}"
#
# info = Car()
# print(info)


# funck_lambda = lambda x, y: x * y
# print("Анонимная функция, помещенная в переменную funck_lambda:", funck_lambda(100, 2))

# class Simple:
#     a = 2
#
#
# y = Simple.a
# print(y)


# Обробка виключень

# try:
#     print(x)
# except:
#     print("Змінна 'x'- не обявлена!")
#
# try:
#     my_func()
#
# except:
#     print("Помилка! Функція не визначена!")


# Множена
# b =[2, 4, 4, 6, 6, 8]
# a = set(b)
# print(a)


# print(emoji.emojize(":thumbs_up: :red_heart:"))#👍 ❤️


# Продвинутые кортежи

# my_tuple = (1, 2, 3, 4, 5)
# a, b, c, d, e = my_tuple
# print(a, b, c, d, e)  # 1 2 3 4 5
# a, *b = my_tuple
# print(a, b)  # 1 [2, 3, 4, 5]

# Обєднання значень списка

# my_list = [['Python', 'Lessons'], ['Django', 'Framework']]
# other_list = sum(my_list, [])
# print(other_list)  # ['Python', 'Lessons', 'Django', 'Framework']

# Другий варіант

# two_list = []
# for element in my_list:
#     for i in element:
#         two_list.append(i)
# print(two_list)  # ['Python', 'Lessons', 'Django', 'Framework']

# Додавання строк

# name = 'Eugene'
# age = 55
# info = 'Hello! {} . You are {} years old'.format(name, age)
# print(info)  # Hello! Eugene . You are 55 years old

# Формуєм середу вивода

# def _print(number, name, age):
#     output = "{:} User {m} is {a} y.o.".format(number, m=name, a=age)
#     print(output)
#
#
# _print(1, 'Eugene', 55)  # 1 User Eugene is 55 y.o.


# Продвинута ітерація автоматичной індексацієй

# programmers = ['Eugene', 'Aleks', 'Jon']
# for index, value in enumerate(programmers):
#     print(f"{index+1}: {value}")
# 1: Eugene
# 2: Aleks
# 3: Jon

# zip() для параллельной итерации по нескольким спискам

# names = ['Petrov', 'Nearonov', 'Balabat']
# grades = [45, 55, 49]
#
# for name, grade in zip(names, grades):
#     print(f"{name} : {grade}")

# Petrov : 45
# Nearonov : 55
# Balabat : 49


#  Создания списков в одну строку

# numbers = range(1, 5)
#
# squares = [number ** 2 for number in numbers]
# print(squares)
# [1, 4, 9, 16]


# any() для проверки наличия элементов, удовлетворяющих условию

# my_str = [23, 5, -5]
# info = any(i < 0 for i in my_str)
# print(info)  # True

# Использование zip() для параллельной обработки нескольких списков

# age = [55, 49, 43]
# name = ['Eugene', 'Natali', 'Vadym']
# my_dict = dict(zip(name, age))
# print(my_dict)
# {'Eugene': 55, 'Natali': 49, 'Vadym': 43}


# Генератор в Python
# def generator(n):
#     for i in range(n):
#         yield i
#
#
# my_generator = generator(5)
# for element in my_generator:
#     print(element, end=" ")
#  0 1 2 3 4


# Что такое *args и **kwargs

# def my_func(a, b, *args):
#     print(a, b, args)
#
#
# my_func(5, 6, 7, 89, 10)
# 5 6 (7, 89, 10)

# def other_func(a, **kwargs):
#     print(a, kwargs)
#
#
# other_func('Eugene', y=4, c=7)
# Eugene {'y': 4, 'c': 7}

# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i)  # 1  3


# Lambda функции

# numbers = (2, 3, 4, 5)
# result = map(lambda a: a * a, numbers)
# print(list(result))

# result = lambda a: a + a
# print(result(10))


# декоратори

# def my_decarator(argument):
#     def func():
#         print("Зявляюсь перед викликом функціі")
#         result = argument()
#         print("Зявляюсь після виклика функціі")
#         return result
#
#     return func
#
#
# @my_decarator
# def my_func():
#     print("Привіт Євген!!! Ти в обертці декоратора @my_decarator")
#
#
# my_func()


#Функция itertools.product() позволяет генерировать
# декартово произведение нескольких последовательностей,
# что может быть полезно, например, при создании всех
# возможных комбинаций элементов из нескольких списков.

one_list = ['red', 'blue', 'green']
two_list = ['S', 'M', 'L']
other_list = list(itertools.product(one_list, two_list))
print(other_list)
