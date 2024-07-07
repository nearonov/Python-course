# my_list = ['ssddf', 'dsf', 12]
# my_tuple = tuple(my_list)
# print(my_tuple)

#ВИЗНАЧЕННЯ ІНДЕКСА В КОРТЕЖЕ

# my_nums = (10, 5, 18, 5, 4, 5)
# index_one = my_nums.index(5)
# index_two = my_nums.index(5, index_one + 1)
# index_three = my_nums.index(5, index_two + 1)
# print(index_one, index_two, index_three)

# my_nums = (10, 5, 18, 5, 4, 5)
# n = 0
# while n < 6:
#     s = my_nums.index(5, n)
#     print(s)
#     n = s + 1


# my_nums = (10, 5, 18, 5, 4, 5)
# n = 0
# for i in range(6):
#     s = my_nums.index(5, n)
#     print(s)
#     n = s + 1

# my_tuple = ([1,2,3], {'first':True, 'second':'abc'})
# other_tuple = (23, 33,67)
# sum_tuple = my_tuple+other_tuple
# print(sum_tuple)

# ----------------------------------
# Распаковка кортежей
# -----------------------------------

# my_tuple = (1, 2, 3)
# first, second, third = my_tuple
# print(first) # 1
# print(second) # 2
# print(third) # 3
# print(my_tuple) # (1, 2, 3)

my_fruits = ('banana', 'apple', 'lime')
my_apple ,*new_fruits = my_fruits
print(my_apple) #banana
print(new_fruits) #['apple', 'lime']
print(my_fruits) #('banana', 'apple', 'lime')