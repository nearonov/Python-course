import sys
from array import array

# a = 'Eugene'

# print("Імя скріпта", sys.argv[0])
# if len(sys.argv)>1:
#     for i in sys.argv:
#         print('аргументи:',i)
# print('\n')
# print(sys.platform)#win32
# print(sys.getsizeof(a),'байт')#55 байт

# sys.argv = ['Eugene', 'Nearonov', 1969]
# def print_args():
#     for i, arg in enumerate(sys.argv):
#         print(f"аргументи {i}:{arg}")
# print_args()




# list = []
# two_array = array('i')
# with open("D:\my_array.bin", 'rb') as my_file:
#     two_array.fromfile(my_file,2)
#     for element in two_array:
#     #print(two_array)
#
#         list.append(element)
# #print(list)
#
# sys.argv = list
#
# first, second = sys.argv
# print(first, second)
# print(sys.argv)

two_array = array('i')
with open("my_array.bin", 'rb') as my_file:
    two_array.fromfile(my_file,4)
    sys.argv=two_array
    for i, element in enumerate(sys.argv):
            print(f'аргумент {i+1}: {element}', end="   ")
