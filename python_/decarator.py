# def decor(func):
#     def wrep_function():
#         print('Я обгортка')
#         func()
#         print('подарунок обгорнутий')
#     return wrep_function
# @decor
# def git_function():
#     print('Я подарунок')
# #print(decor(git_function))
# print(git_function())

# def smart_div(func):
#     def wrapper(a, b):
#         print("Я буду ділити", a ,"на", b)
#         if b == 0:
#             print("На нуль ділить неможна!")
#             return
#         return func(a, b)
#
#     return wrapper
# @smart_div
# def div_smart(a, b):
#     return a/b
# print(div_smart(6, 2))


# def make_sendwich(funс):
#     def wraper(arg):
#         print('хліб')
#         funс(arg)
#         print('хліб')
#     return wraper
#
#
# @make_sendwich
# def sendwich(arg):
#     print(arg)
# sendwich('М ясо')
# хліб
# М ясо
# хліб

# Клас-декоратор
# class cover_decorator():
#     def __init__(self, cover):
#         self.cover = cover
#
#     def __call__(self, func):
#         def wraper(arg):
#             print(self.cover)
#             func(arg)
#             print(self.cover)
#
#         return wraper
#
#
# @cover_decorator('хліб')
# @cover_decorator('салат')
# def sengwich(arg):
#     print(arg)
#
#
# sengwich('м ясо')


# Декоратори з параметрами
# def make_sandwich(sandwich_cover):
#     def decorator(funk):
#         def wraper(arg):
#             print(sandwich_cover)
#             funk(arg)
#             print(sandwich_cover)
#         return wraper
#     return decorator
# @make_sandwich('хліб')
# @make_sandwich('салат')
# def my_sendwich(arg):
#     print(arg)
#
# my_sendwich('ковбаса')

# def function(func):
#     def wraper(*args, **kwargs):
#         print("Обгортка моєй функціі")
#         func(*args, **kwargs)
#         print('Я обгорнув мою функцию обгорткой')
#         return func(*args, **kwargs)
#
#     return wraper
#
#
# @function
# def my_function(a, b):
#     print("Thi is my function")
#     return (a, b)
# x = my_function(3, 20)
# print(x)


# Логірованіє даних

# def log_function(fn):
#     def wraper(*args, **kwargs):
#         print(f"Name function: {fn.__name__}")
#         print(f"function argument:{args}{kwargs}")
#         result = fn(*args, **kwargs)
#         print(f"result function :{result}")
#         return result
#     return wraper
# @log_function
# def my_function(a, b):
#     return a*b
# print(my_function(3,b=2))


# Перевірка аргументів


# def valide_arg(fn):
#     def wraper(*args,**kwargs):
#         for arg in [*args,*kwargs.values()]:
#             if not isinstance(arg,int) and not isinstance(arg,float):
#                 raise ValueError(f'Тип {arg} є {type(arg)}. Всі аргументи має бути int або float')
#
#         result = fn(*args, **kwargs)
#         return result
#     return wraper
#
# @valide_arg
# def my_function(a,b):
#     return a+b
# try:
#     print(my_function(3,b=5))
# except ValueError as e :
#     print(e)


# Перевірка аунтефікаціі пользователя

# def aut_user():
#     return True
#
# def check_aut_user(func):
#     def wraper(*args, **kwargs):
#         if aut_user():
#             print("Користувач аутентіфіцирован!")
#             return func(*args, **kwargs)
#         else:
#             raise ValueError("Користувач не аутентіфіцирован!")
#     return wraper
# @check_aut_user
# def my_function():
#     print("Сервер запущен!")
# try:
#     my_function()
# except ValueError as e :
#     print(e)


