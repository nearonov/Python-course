# my_dict = {}
# if my_dict:
#     print(not not my_dict, "my_dict - правдиве")
# else:
#     print(not not my_dict, "my_dict - ложне")
# # False my_dict - ложне

# my_dict = {'name':'Eugene'}
# if not my_dict.get('name'):
#     print(True)
#
# else:
#     print(False)
#     print('My name is', my_dict['name'])

# my_number = -1
# if my_number < 0:
#     print(my_number, "є відємним числом")
# elif my_number > 0:
#     print(my_number, "є додатнім числом")
# else:
#     print(my_number, "є нулем")


# def nums_info(a, b):
#     if type(a) is not int or type(b) is not int:
#         return ("Число a або b не є цілим числом")
#     if a>=b:
#         return f"Число {a} більше, або дорывнює числу {b}"
#     return f"Число {a} меньше числа {b}"
#
# print(nums_info(4,3))

# || способ

# def nums_info(a, b):
#     if type(a) is not int or type(b) is not int:
#         info = ("Число a або b не є цілим числом")
#
#     elif a >= b:
#         info = f"Число {a} більше, або дорывнює числу {b}"
#     else:
#         info = f"Число {a} меньше числа {b}"
#     return info
#
# print(nums_info(4,3))

# def route_info(arg):
#     if arg.get('distance') and isinstance(arg['distance'], int):
#         # if 'distance' in arg and type(arg['distance'])==int:
#         return f"Distance to your destination is {arg['distance']} km."
#     if arg.get('speed') and arg.get('time') \
#             and isinstance(arg['speed'], int) \
#             and isinstance(arg['time'], int):
#         return f"Distance to your destination is {arg['speed'] * arg['time']} km."
#     return "No distance info is available"
#
#
# print(route_info({'distance': 70, 'speed': 40, 'time': 2}))
# # Distance to your destination is 70 km.
# print(route_info({'distance': 70.2, 'speed': 40, 'time': 2}))
# # Distance to your destination is 80 km.
# print(route_info({'distanc': 70.0, 'speeds': 40, 'times': 2}))
# # No distance info is available

# || способ

def route_info(arg):
    if 'distance' in arg and type(arg['distance']) == int:
        info = f"Distance to your destination is {arg['distance']} km."
    elif 'speed' in arg and 'time' in arg \
            and type(arg['speed']) == int \
            and type(arg['time']) == int:
        info = f"Distance to your destination is {arg['speed'] * arg['time']} km."
    else:
        info = "No distance info is available"
    return info

print(route_info({'distance': 70, 'speed': 40, 'time': 2}))
# Distance to your destination is 70 km.
print(route_info({'distance': 70.2, 'speed': 40, 'time': 2}))
# Distance to your destination is 80 km.
print(route_info({'distanc': 70.0, 'speeds': 40, 'times': 2}))
# No distance info is available