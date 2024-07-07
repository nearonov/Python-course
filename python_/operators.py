# not, and, or - логічні оператори
# is, is not, not, not in

# a = 10
# b = a
#
# c = a + b
# print(a is b) # True
# print(c is a) # False


# my_bool = True
# other_bool = False
# print(+my_bool) # 1
# print(+other_bool) # 0
#
# a = 10
# b = 0
# print(not a) # False
# print(not b) # True


# my_dict ={'name':'Eugene', 'age':54}
# print('age'in my_dict) # True
# print('asd'in my_dict) # False
# print('name' not in my_dict) # False

#------------------------------------------------
# Практичне
#------------------------------------------------

# my_set = {23, True,'Eugene'}
# other_set = {23, True,'Eugene'}
# print(my_set==other_set) #True оператор == порівнює значення ,а не id
#                          # за допомогой магического метода наборів
# print(my_set.__eq__(other_set)) #True
# print(my_set!=other_set) #False

# print(my_set is other_set) #False  is порівнює обєкти (id) ,а не значення
# print(id(my_set))    # 2232691826848
# print(id(other_set)) # 2232691823712
#
# print(True in my_set)   #True
# print(not 'Eugene'in other_set) #False

#-----------------------------------------------
#Ложні значення
#---------------------------------------------------
# ВСІ ПУСТІ ПОСЛІДОВНОСТІ ЯВЛБЮТСЯ ЛОЖНІ False
# print(bool({}))#False
# print(not not({}))#False
# print(bool(set()))#False
#
# my_list = ['qwe',23]
#
# if my_list:
#     print('Правдиве значення')
# else:
#     print('Ложне значення')

#-----------------------------
#DEL - ІНСТРУКЦІЯ ,А НЕ ОПЕРАТОР !!!
#-------------------------------

# button_style = {
#      'brand': 'Dukati',
#      'price': 25000,
#      'engine_vol': 1.2,
#  }
# del button_style['price']
# print(button_style)
# # {'brand': 'Dukati', 'engine_vol': 1.2}

# my_list = ['asd','Eugene', True, 23,[1.2]]
# del my_list[1:3]
# print(my_list)
# ['asd', 23, [1.2]]
