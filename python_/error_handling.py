#--------------------------------
# ОБОБКА ПОМИЛОК
#--------------------------------
# try:
#     a = int(input("Ввести ціле чисо :"))
#     b = 20/a
#     print(b)
# except ValueError :
#         print("Помилка ! Ви ввели строку ,а не ціле число")
# except ZeroDivisionError as e:
#         print(e) # division by zero
#         print("На нульь ділить не можна!!!")
#
# else: # блок else виконуєтся якщо не виникла помилка
#     print(20+a)
# finally: # блок finally виконуєтся в любому випадку
#     print('Continue.......')

#---------------------------------------
#ГЕНЕРАЦІЯ ПОМИЛОК ЗА ДОПОМОГОЙ raise
#----------------------------------------
# def division_nums(a, b):
#     if b==0:
#         raise TypeError("Другий аргумент не повинен дорівнювати '0'")
#     return a/b
#
# try:
#     d=20
#     f=0
#
#     info = division_nums(d,f)
#     print(info)
# except Exception as e:
#     print(e)

#---------------------------------------
#Завдання
#---------------------------------------

def image_info(**dict):
     if  'image_title'  not in dict or 'image_id' not in dict :
        raise TypeError("Відсутній один з ключів 'image_title', 'image_id' ")
     info = f"Image {dict['image_title']} has id {dict['image_id']}"
     return info

try:
    my_dict =image_info(image_title="'my cat'", image_id=5136)
    print(my_dict)
except TypeError as e :
     print(e)

