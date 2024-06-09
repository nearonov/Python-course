# r = 'Hello Eugene'
# b = '3345'
# list_r=list(r)
# list_r.append((list(b))[0:2])
# del list_r[0]
# print(list_r, "Довжина списку: ",len(list_r))
# print(dir(list))

# my_fruit = 'apple'
# other_fruit = 'banan'
# new_fruit = 'lime'
# all_fruit = [my_fruit, other_fruit, new_fruit]
# print(all_fruit)

# КОПІЮВАННЯ СПИСКІВ

# my_fruit = ['apple']
# copied_fruit = my_fruit
# copied_fruit.append('lime')
# print(my_fruit)
# print(copied_fruit)
# print(id(my_fruit)==id(copied_fruit)) #True

# my_cars = ['BMV']
# copied_cars = my_cars[:]
# copied_cars.append('Audi')
# print(my_cars)
# print(copied_cars)
# print(id(my_cars)==id(copied_cars))#False

# my_cars = ['BMV']
# copied_cars = my_cars.copy()
# copied_cars.append('Audi')
# print(my_cars)
# print(copied_cars)
# print(id(my_cars)==id(copied_cars)) #False

# my_cars = ['BMV']
# copied_cars = list(my_cars)
# copied_cars.append('Audi')
# print(my_cars)
# print(copied_cars)
# print(id(my_cars)==id(copied_cars))#False

# my_list = ['eugene', 100, True, {'a': 22}, 50.5]
# del my_list[2]
# print(my_list, 'Довжина списка:', len(my_list))
# my_list.reverse()
# print(my_list)
# other_list = ['abc',True]
# my_list.extend(other_list)
# print(my_list)
# print(other_list)
#
# one_list = [1,5]
# two_list = [7,9]
# three_list = one_list + two_list
# print(three_list)
# print(one_list.__add__(two_list))
