# my_number = 23
# print("my_number is int") if type(my_number) is int else print("is not int" )

# temp = -1
# wether = "hot" if temp > 18 else 'cold'
# print(wether)
# cold

# my_img = ('1920', '1080')
# a, b = my_img
# info = f"{a} x {b}" if len(my_img) == 2 and type(a)==str and \
#                             type(b)==str else 'incorrect image formatting'
# print(info)

# || способ

# other_img = ('1920', '1080')
#
# if len(other_img)==2  and type(other_img[0])==str and type(other_img[1])==str :
#     info = (f"{other_img[0]} x {other_img[1]}")
# else:
#     info = 'incorrect image formatting'
# print(info)


info = input("Ввести текст :")
a = "string is long" if len(info)>79 else "string is short"
print(a)
