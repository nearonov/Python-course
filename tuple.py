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

my_tuple = ([1,2,3], {'first':True, 'second':'abc'})
other_tuple = (23, 33,67)
sum_tuple = my_tuple+other_tuple
print(sum_tuple)