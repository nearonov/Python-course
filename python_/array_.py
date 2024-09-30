from array import array

# a = array('d', [1.1, 3.5, 4.5])
# print(a)
# print(a[1])  # 3.5
#
# my_array = array('i', [23, 34, 44])
# other_array = array('i', [22, 33, 43])
# # sum_array = array('i')#пустий масив цылих чисел
# sum_array = my_array + other_array  # обєднання двох масивов
# print(sum_array)#array('i', [23, 34, 44, 22, 33, 43])
#
# del sum_array[:-1]#видалення елементів масиву
# print(sum_array)#array('i', [43])
#
# sum_array.remove(43)#метод для видалення заданого елемента
# print(sum_array)#array('i')
#
# ar = array('i', [54,54,3])
# ar.append(3)
# x = ar.count(54)
# z = ar.__len__()
# print(ar)
# print(f"кількість елементів 54: {x}")
# print(f"загальна кількість елементів: {z}")
# for element in ar:
#     print(element, end=" ")
#
# ar.reverse()
# print('\n')
# print(ar)

#зберигти масив в файле
one_array = array('i', [23, 54, 67, 73])
with open("D:\my_array.bin", 'wb') as my_file:
    one_array.tofile(my_file)

#прочитати масив з файлу
two_array = array('i')
with open("D:\my_array.bin", 'rb') as my_file:
    two_array.fromfile(my_file,2)
    print(two_array)