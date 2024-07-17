# my_fruits = {"apple", "banana", "lime"}
# other_fruits = {"banana", "lime", "apple"}
# my_numbers = {12, 23, 44}
# print(my_fruits == other_fruits)
# #True
# sum_fruits = my_fruits.union(my_numbers)
# print(sum_fruits,'\n', "Довжина набору:",  len(sum_fruits))

# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}
# print(my_set.intersection(other_set))
# #{'f', 'd'}
# print(my_set.intersection('abcd'))
# #{'d'}
# print(my_set.intersection(['abcd', 'y']))
# #{'y'}
# print(my_set.union(other_set))
# #{'a', 'd', 'abc', 'y', 'f'}
# print(other_set.issubset(my_set))
# #False

# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}
# print(my_set.difference(other_set))
# #{'y', 'abc'} Різниця
# print(my_set.discard('abc'), my_set)
#None {'d', 'f', 'y'} Видалення елемента

# my_set = {'abc', 'd', 'f', 'y'}
# copy_set = my_set.copy() #копіювання
# my_set.add('Eugene')
# copy_set.add('Nearonov')
# print(my_set)
# #{'abc', 'Eugene', 'y', 'f', 'd'}
# print(copy_set)
# #{'Nearonov', 'abc', 'y', 'f', 'd'}
# print(my_set.intersection(copy_set))#перетен двох множин спільні елемеенти
# #{'f', 'd', 'y', 'abc'}

# a={'a', 'd', 'f','y'}
# b = {'a', 'd', 'f','l'}
# print(a.symmetric_difference(b))
# #{'y', 'l'} сіметрична різниця - елементи які є в одном і не має
#             #в другому і є в другому і не має в першому

my_set = {1,2,6,9}
my_set.add(100)
other_set = {2,34,9,45}
new_set = my_set.intersection(other_set)
print(list(new_set))
print(my_set)
#[9, 2]
