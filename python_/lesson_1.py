# name = 'Eugene'
# print(dir(name))
# print(name.upper())

#
# a = 12
# b = 20
# a, b = b, a
# print('a=', a, 'b=', b)


# name = 'Eugene'
# print('name=  ', id(name))
#
# soname = name
# print('soname=', id(soname))

# строки

# info_msg = """Привіт
# Євген
# Удачи!!!"""
# print(info_msg)
# Привіт
# Євген
# Удачи!!!

# срези
# r = "Im Winter hell bis sonnig, im Sommer leicht schattiert, auch im Garten möglich"
# print(r[10:-1])

# number = int(input("Введіть число:"))
# print(number)
# print(type(number))
# n = float(number)
# print(n)
# print(type(n))

# степінь числа

# base = 3
# pover = 5
# print(pow(base, pover))


# комплексні числа

# complex_a=4 + 5j
# complex_b=7 + 6j
# sum=complex_a+complex_b
# print(sum)
# print(type(sum))


# тип bool

# print(12>11)
# print('nuts'>'nata')

# Зміна обєктів в Python

# from copy import deepcopy
# my_list = {1:True,2:[]}
# other_list = {1:True}
# other_list = my_list
# other_list = deepcopy(my_list) #Глубока копія
# other_list = my_list.copy() # Повірхнева копія
# other_list [2].append('Eugene')
# print(id(my_list), my_list)
# print(id(other_list),other_list)

# -----------------------------------
# Зєднання строк
# ------------------------------------

# print('Eugene '+'Nearonov')
# # Eugene Nearonov
# print('Eugene '.__add__('Nearonov'))
# # Eugene Nearonov

# -----------------------------------
# Форматування строк - f строки
# ------------------------------------
# soname = 'Eugene'
# name = 'Nearonov'
# sn = f"{soname} {name}"
# print(sn)
# Eugene Nearonov


# name = 'eugene'
# hoby ='bicycle'
# city = 'rivne'
# time_wan = 8
# time_tow = 10
# info = f"i'm {name}, i like to ride a {hoby} around the city {city} from {time_wan} am to {time_tow} pm.".title()
# print(info)
# I'M Eugene, I Like To Ride A Bicycle Around The City Rivne From 8 Am To 10 Pm.

