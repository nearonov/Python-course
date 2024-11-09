# def hello(name):
#     print('Hello', name)
#
# hello('Eugene')

# def sum_nums(a, b):
#     sum = a + b
#     return sum
#
# r=sum_nums(3, 10)
# print(r)

# def list(a):
#     my_list = []
#     my_list.append(a)
#     return my_list
#
#
# for n in range(3):
#     a = input('Ввести елемєнти списку:')
#     b=list(a)
# print(b)

# Передача в функцію ізменяемого обєкта
# Зовнішній обєкт змінится (небажено)
# def person_age(person):
#     print('id person:',id(person))
#     person['age']+=1
#     return person
#
# person_one = {'name':'Bob', 'age':21}
# print('id person_one:',id(person_one))
#
# person_age( person_one)
# print(person_one)

# Запобігання зміни зовнішнього обєкта

# def person_age(person):
#     print('id person:',id(person))
#     copy_person = person.copy()
#     copy_person['age']+=1
#     return copy_person
#
# person_one = {'name':'Bob', 'age':21}
# print('id person_one:',id(person_one))
#
# new_person_one=person_age( person_one)
# print(person_one)
# print(new_person_one)
# print('id:', id((new_person_one)))

# ----------------------------------------------------------------
# Завдання
# -----------------------------------------------------------------

# def merge_lists_to_dict(list_1,list_2):
#     return dict(zip(list_1,list_2))
#
# # name = ['Nearonov', 'Balabat']
# # age = [54,49]
# # r=merge_lists_to_dict(name,age)
# # print(r)
# #
# print(merge_lists_to_dict(['Nearonov'], list_2=[54,49]))
# # {'Nearonov': 54}
#
# print(merge_lists_to_dict(list_2=[54,49], list_1=['Nearonov']))
# # {'Nearonov': 54}
#
# info=merge_lists_to_dict(list_1=['Eugene', 'Natalia'], list_2= [54,49])
# print(info)
# {'Eugene': 54, 'Natalia': 49}

# print(merge_lists_to_dict(list_1=['Nearonov'], [54,49]))
# SyntaxError: positional argument follows keyword argument

# -----------------------------------------------------------------
# Обєднання аргументів в кортеж
# --------------------------------------------------------------------

# def sum_nums(*args):
#     print(args)
#     print(args[0])
#     return sum(args)
#
# print(sum_nums(2,3))
# (2, 3)
# 2
# 5

# Аргументи с ключевими словами
# def get_post(name,posts_qty):
#     info = f"Привіт {name} тобі {posts_qty} років. "
#     return info
#
# i = get_post(name='Євген', posts_qty=54)
# print(i)
# Привіт Євген тобі 54 років.

# --------------------------------------------------------------------------------
# Обєднання аргументів в словник
# -------------------------------------------------------------------------

# def get_posts(**kwargs):
#     print(kwargs)
#     # {'name': 'Eugene', 'posts_qty': 25}
#     print(type(kwargs))
#     # <class 'dict'>
#     info = (
#             f"{kwargs['name']} написав "
#             f"{kwargs['posts_qty']} постов"
#     )
#     return info
#
# info = get_posts(name='Eugene', posts_qty=25)
# print(info)
# Eugene написав 25 постов

# ---------------------------------------------------------------
# Завдання
# ------------------------------------------------------------------
# def update_car_info(**car):
#     car['is_available'] = True
#     return car
#     # info = f"{car['brand']}  {car['price']} UAH"
#     # return info
#
# print(update_car_info(brand='BMW', price=250000 ))

# -------------------------------------------------------------------
# Значення параметров фунціі по замовченням
# -------------------------------------------------------------------

# def mult_by_factor(value, multiplier=1):
#     return value * multiplier


# print(mult_by_factor(5))
# # 5
# print(mult_by_factor(5, 3))
# # 15

# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_new_post(post, weekday=get_weekday()):
#     copy_post = post.copy()
#     copy_post['created_on_weekend'] = weekday
#     return copy_post
#
#
# inital_post = {'id': 243, 'name': 'Eugene'}
# print(create_new_post(inital_post))
# # {'id': 243, 'name': 'Eugene', 'created_on_weekend': 'Thursday'}
#
# res=date.today()
# print('поточна дата:',res) #повертає поточну дату
# print('поточний день:',res.day)#повертає поточний день
# print('поточний місяц:',res.month)#повертає поточний місяц
# print('поточний рік:',res.year)

# ----------------------------------------------------------------------
# Колбек функціі
# ----------------------------------------------------------------------
# def numbs_info(num):
#
#     if num % 2 == 0:
#         print(num, "number is even")
#     else:
#         print(num, "number no even")
#
#
# def prosses_info(num, callback):
#     """definition of even number"""
#     callback(num)
#
#
# n = int(input("Ввести число: "))
# prosses_info(n, numbs_info)

# ---------------------------------------------------------
# Глобальні і локальні змінні і їх видимість
# ---------------------------------------------------------
# a = 10
#
#
# def my_fn():
#     global a
#     a = 5
#
#
# my_fn()
# print(a)

# -----------------------------------------
# lambda  функція
# -----------------------------------------

mult = lambda a, b: a * b
print(mult(3, 5))

# def get_info(name):
#     return lambda gate :f"{gate} {name}"
#
# info = get_info('Eugene')
# print(info('Hello!'))
#
# moning=get_info('Eugene')
# print(moning("Goog moning"))


# print(f"__name__ = {__name__}")

# def func():
#     print("Функція відпрацювала!")
#
# if __name__ == "__main__":
#     func()

# Рекурсивная функція
# def fuc(a):
#     if type(a) is not int:
#         raise TypeError('Числа повинні бути цілими')
#     if a <= 0:
#         raise ValueError('Числа повинні бути позитивними')
#     if a == 1:
#         return 1
#     print(a)
#     return fuc(a - 1) * a
#
#
# print(fuc(5))
# def sum(s):
#     print(s)
#     if not s:
#         return 0
#     else:
#         return s[0]+ sum(s[1:])
# j = [3, 5, 6, 9]
# print(sum(j))


# Две звездочки  перед объектом словаря позволяют
# передать содержимое словаря как аргументы.
# Где ключи словаря - имя аргумента, а значения
# передаются в функцию

# my_dict = {'name': 'Eugene', 'soname': 'Nearonov'}
#
#
# def info(name, soname):
#     return f"{name} {soname}"
#
#
# print(info(**my_dict))
