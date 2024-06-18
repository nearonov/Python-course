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

#Передача в функцію ізменяемого обєкта
#Зовнішній обєкт змінится (небажено)
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

#Запобігання зміни зовнішнього обєкта

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

#----------------------------------------------------------------
#Завдання

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

#-----------------------------------------------------------------
# Обєднання аргументів в кортеж

# def sum_nums(*args):
#     print(args)
#     print(args[0])
#     return sum(args)
#
# print(sum_nums(2,3))
# (2, 3)
# 2
# 5

#Аргументи с ключевими словами
# def get_post(name,posts_qty):
#     info = f"Привіт {name} тобі {posts_qty} років. "
#     return info
#
# i = get_post(name='Євген', posts_qty=54)
# print(i)
#Привіт Євген тобі 54 років.

#--------------------------------------------------------------------------------
# Обєднання аргументів в словник

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

def update_car_info(**car):
    car['is_available'] = True
    return car
    # info = f"{car['brand']}  {car['price']} UAH"
    # return info

print(update_car_info(brand='BMW', price=250000 ))


