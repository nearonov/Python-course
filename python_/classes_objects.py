# class Frutis:
#     name = ('apple', 'lime', 'banan')
#
#     def move(self):
#         return "Hello Eugene!"
#
#
# my_frutis = Frutis()
# print(isinstance(my_frutis, Frutis))  # True
# print(type(my_frutis))  # <class '__main__.frutis'>
# print(my_frutis.move())  # Hello Eugene!
# print(Frutis.name)  # ('apple', 'lime', 'banan')
# print(Frutis.move(my_frutis))  # Hello Eugene!


# class Comment:
#     def __init__(self, info):
#         self.info = info
#         self.votes_qty = 0

# def votes(self, qty):
#     self.votes_qty += qty
#
# def reset_votes(self):
#     self.votes_qty = 0


# first_comment = Comment('Hello Eugene!')
# print(type(first_comment)) # <class '__main__.Comment'>
# print(first_comment.info)  # Hello Eugene!


# print(first_comment.votes_qty) # 0
# first_comment.votes(5)
# print(first_comment.votes_qty) # 5
# first_comment.reset_votes()
# print(first_comment.votes_qty) # 0


# class FirstClass:
#     def setdata(self, valu):
#         self.data = valu
#
#
#     # def __init__(self,valu):
#     #     self.data=valu
#
#     def display(self):
#         print(self.data)
#
#
# # x = FirstClass('Hello Eugene!')
# x = FirstClass()
# x.setdata(40)
# # print(x.data)
# # y.setdata(3.14)
# print(x.data)


# class SecondClass(FirstClass):
#     def display(self):
#         print('Current value ="%s"' % self.data)
#
#
# z = SecondClass()
# z.setdata(42)
# print(z.display())


# class Dog:
#     species = "Canis familiaris"  #атрібут класа
#
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color
#
#     def __str__(self):
#         return f"Ім я собаки {self.name} ,а вік собаки {self.age} років.\n" \
#                f"{self.name}'s coat is {self.coat_color}."
#
#
# dog_one = Dog('Chack', 12, 'brown')
# print(dog_one.name, dog_one.age)  # chack 12
# print(dog_one.species)  # Canis familiaris
# dog_one.age = 13  # значения можно менять динамически
# print(dog_one.age)  # 13
# print(dog_one)  # Ім я собаки chack ,а вік собаки 13 років.
#
#
# class Car:
#     def __init__(self, color, mileage=0):
#         self.color = color
#         self.mileage = mileage
#
#     def drive(self,arg):
#         self.mileage += arg
#
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage} milles."
#
#
# car_one = Car('blue', 0)
# car_tow = Car('red', 0)
# car_one.drive(100)
# car_tow.drive(200)
# print(car_one)
# print(car_tow)

# class Image:
#     total_images = 0
#
#     def __init__(self, resolution, title, extension):
#         self.resolution = resolution
#         self.title = title
#         self.extension = extension
#         Image.total_images += 1
#
#     def resize(self, arg):
#         self.resolution = arg
#
#     @staticmethod  # декоратор який не привязуе метод merg_comments до екземпляру (self)
#     def merg_comments(first, second):
#         return f"{first} {second}"
#
#     def __str__(self):
#         return f"разрішення зображення {self.resolution} {self.title} " \
#                f"розширення {self.extension} кількість зображень {Image.total_images}"
#
#
# format_one = Image("860 x 860", 'Istagram', 'JPG')
# format_two = Image("3040 x 2010", "facebook", "png")
# format_one.resize("1920 x 720")
# format_two.resize("1366 x 768")
# my_comment = Image("3040 x 2010", "facebook", "png")
# print(format_one)
# print(format_two)
# print(Image.merg_comments('Hello!!', 'Eugene'))  # Hello!! Eugene
# print(my_comment.merg_comments('Hello!!', 'Eugene'))  # Hello!! Eugene

# class Comment:
#     def __init__(self, info):
#         self.info = info
#         self.votes_qty = 0
#
#     def votes(self, qty):
#         self.votes_qty += qty
#
#     def reset_votes(self):
#         self.votes_qty = 0
#
#     def __str__(self):  # саморуч створюємо метод довання
#         return (f"{self.info} {self.votes_qty} години в день")
#
#     def __add__(self, other):
#         return f"{self.info} {other.info}", self.votes_qty + other.votes_qty
#
#     def __eq__(self, other):# саморуч створюємо метод порівняння
#         if self.info == other.info and self.votes_qty == other.votes_qty :
#             return True
#         return False
#
#
# one_comment = Comment("Я програмую")
# one_comment.votes(2)
# two_comment = Comment("мова програмуввання Python")
#
# print(one_comment)  # Я програмую 2 години в день
# two_comment.votes(1)
# print(two_comment)
# sum = one_comment + two_comment
# print(sum)
# print(one_comment == two_comment)#False
# a = Comment('asd')
# b = Comment('asd')
# a.votes(1)
# b.votes(1)
# print(a == b)#True

class ExtendedList(list):
    def print_info_list(self):
        print(f"list has {len(self)} elements")
        #return (f"list has {len(self)} elements")
my_list = ExtendedList(['Eugene', 'Nataliy', 'Bogdan'])
my_list.print_info_list() #list has 3 elements
my_list.append('Ivan')
my_list.print_info_list() #list has 4 elements
# Єархія класів: my_list-> ExtendedList -> list -> object