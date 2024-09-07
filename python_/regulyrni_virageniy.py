import re
import time

# my_files = "My name is Eugene."
# a = re.search('E....e\.', my_files)
# b = re.search('^M.*name',my_files)
# print(a)#span=(11, 18), match='Eugene.'
# print(b)#span=(0, 7), match='My name'
# print('E....e\n.')
# print(r'E....e\n.')# 'r ' не дає \n  перенести'.' на другу стоку
# print(a.span())#(11, 18)
# print(a.start())#11
# print(a.end())#18

# Сберігання патерна в окремом обєктію

# files = "My name is Eugene."
# file = "My name is Eugene. Eugene is instructor."
# my_patern = re.compile(r"Eugene\.$")
# patern = re.compile(r"My.*\.$")
# other_patern = re.compile(r'E....e')
# print(my_patern.search(files))
# print(patern.match(files))#span=(0, 18), match='My name is Eugene.'
# print(other_patern.findall(file))#['Eugene', 'Eugene']

# Перевірка email

# def check_eml(eml):
#     a = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.+[a-zA-Z0-9-.]+$"
#     patrn = re.compile(a)
#     return (eml, 'eml valid' if patrn.fullmatch(eml) else "eml not valid")
#
# print(check_eml("ayvengo85gmail.com"))


# files = 'telefon 123-12-45 , my adres 67.56.98.74'
# patern = re.compile(r"\d\d\D\d\d")

# for i in patern.finditer(files):
#     print(i[0])
#     #23 - 12
#     #67.56
#     #98.74
# print(patern.findall(files))#['23-12', '67.56', '98.74']
# print(re.sub(r'\d\d\d\D\d\d\D\d\d', r'02.08.2024 ',files))#telefon 02.08.2024  , my adres 67.56.98.74
# print(re.findall(r'[ertyui]+', r'EEEEE rrrr TTTTTT YYYY iiii', flags=re.IGNORECASE))
# ['EEEEE', 'rrrr', 'TTTTTT', 'YYYY', 'iiii']


# text = "Телфон МТС 87-926-123-12-12, телефон Київстар 8-11-22-555-666"
# other_patern = re.compile('(?:7|8)(?:-\d{2,4}){4}')
# print(other_patern.findall(text))#['7-926-123-12-12', '8-11-22-555-666']


# match = re.search(r'\w+.*', r'$$ What Ho')
# print(match[0])#What Ho


# my_files = "--  Eugene55  --  Nearonov55"
# my_patern = r'\s+([a-zA-Z]+)(\d+)\s+\S+\s+([a-zA-Z]+)'
# match = re.search(my_patern, my_files)
# print(match[0])# Eugene55  --  Nearonov
# print(f'група букв {match[1]} с позиціі {match.start(1)} до {match.end(1)}')#група букв Eugene с позиціі 4 до 10
# print(f'група цифр {match[2]} с позиціі {match.start(2)} до {match.end(2)}')#група цифр 55 с позиціі 10 до 12
# print(match[3])#Nearonov


# string = "1234567987"
# patern_won =re.compile(r"((\d)(\d))((\d)(\d))")
# match = patern_won.search(string)
# print(match[1])#12
# for i in range(0,7):
#     print(f"Група №{i} >{match[i]}< з позиціі"
#           f" {match.start(i)} до {match.end(i)}", end="  ")
# Група №0 >1234< з позиціі 0 до 4  Група №1 >12< з позиціі 0 до 2
# Група №2 >1< з позиціі 0 до 1  Група №3 >2< з позиціі 1 до 2
# Група №4 >34< з позиціі 2 до 4  Група №5 >3< з позиціі 2 до 3
# Група №6 >4< з позиціі 3 до 4

# print(re.findall(r"([A-Za-z]+)(\d*)",r"For344, go, fg3"))
# [('For', '344'), ('go', ''), ('fg', '3')]


# print(re.split(r"(\s*)([/+*-])(\s*)",r"12+2 / 45"))#['12', '', '+', '', '2', ' ', '/', ' ', '45']
# print(re.split(r"\s*([/+*-])\s*",r"12+2 / 45"))#['12', '+', '2', '/', '45']

# st = 'мороз и солнце, день чудесный'
# patern = re.compile(r"\s")
# print(patern.split(st))#['мороз', 'и', 'солнце,', 'день', 'чудесный']


# Використування груп для заміни
# text = r"Свою дату 16.08.1969. хочу змінити РРРР.ММ.ДД"
# patern =re.compile(r"(\d\d).(\d\d).(\d{4})")
# match = patern.sub(r"\3.\2.\1", text)
# print(match)#Свою дату 1969.08.16. хочу змінити РРРР.ММ.ДД

# text = "E@u#gene he%&llo!"
# patern = re.compile(r"[^A-Za-z.!? \n]")
# m = patern.sub('',text)
# print(m)#Eugene hello!

# start = time.time()
# with open("D:\книги\Python\django\реєст_нового_користувача.txt", 'r',encoding='utf8')as boock:
#     patern = re.compile(r"\\eugene\\")
#     result = [line for line in boock if patern.findall(line)]
# print(f"Знайдено {len(result)} співпадінь, заняв час пошуку {time.time() - start}")
# Знайдено 7 співпадінь, заняв час пошуку 0.017008543014526367

# text = "Hello 3, Eugene 5!, привет!"
# patern = re.compile( r"3|5")
# other_patern = re.compile(r'e\B')
# print(patern.findall(text))#['3', '5']
# print(other_patern.findall(text))#['e', 'e']

# st = 'Почему-то часто никак как-то получилось что-то зачем-то опять Кто-то'
# patern = re.compile(r"\b\w+-\w+\b")
# print(patern.findall(st))#['Почему-то', 'как-то', 'что-то', 'зачем-то', 'Кто-то']

# st = 'Книга компьютер крот колобок колхоз' \
#      ' кооперация ноутбук карандаш координатор'
# patern = re.compile(r"ко{1,2}")
# print(f"Кількість слів :{len(patern.findall(st))}")#Кількість слів :5

# st = '"Это" - фрагмент текста, для обработки?!..'
# patern = re.compile(r"[^А-Яа-я0-9- \n]")
# print(patern.sub("", st))#Это - фрагмент текста для обработки

#https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-16-regulyarnye-vyrazheniya-2023-02-20
#Напишите регулярное выражение, которое находит в
# полученной от пользователя строке все слова,
# содержащие подстроку «круж», но не в начале и не в конце слова.

# st = 'окружность кружево кружка окружение' \
#      ' головокружение кружок кружкруж'
# patern = re.compile(r"\b\w+круж\w+\b")
# print(patern.findall(st))#['окружность', 'окружение', 'головокружение']

# меняет формат даты в URL с ГГГГ/ММ/ДД на ДД.ММ.ГГГГ.
# st ="https://www.washingtonpost.com/technology/2023/02/14/what-is-temu-super-bowl-commercial/"
# patern = re.compile(r"(\d{4})/(\d\d)/(\d\d)")
# print(patern.sub(r'\3.\2.\1', st))

# Завдання
# Перевірка валідності пароля

# def check_pasword(pasword):
#     # a = r'^[a-zA-Z0-9.!#@$%&]{8,}+$'
#     # b = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!#@$%&])"
#     # patern_one = re.compile(a)
#     # patern_two = re.compile(b)
#     patern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!#@$%&])[a-zA-Z0-9.!#@$%&]{8,}$")
#     # return True if patern_one.fullmatch(pasword)and patern_two.match(pasword) else False
#     return True if patern.fullmatch(pasword)else False
# print(check_pasword('Q2G32Dd4!'))

# def check_pasword(pasword):
#     len_patern = re.compile(r"\S{8,}")
#     lowercase_patern = re.compile(r"^.*[a-z]+.*$")
#     uppercase_patern = re.compile(r"^.*[A-Z]+.*$")
#     number_patern = re.compile(r"^.*[0-9]+.*$")
#     symbols_patern = re.compile(r"^.*[!#@$%&]+.*$")
#     space_patern = re.compile(r"^\S*$")
#     if not space_patern.fullmatch(pasword):
#         return (False, "Пароль  має пробіл")
#     if not len_patern.fullmatch(pasword):
#         return (False, "Пароль має меньше 8 символів!")
#     if not lowercase_patern.fullmatch(pasword):
#         return (False, "Пароль не має букв в нижньому регістрі")
#     if not uppercase_patern.fullmatch(pasword):
#         return (False, "Пароль не має букв в верхньому регістрі")
#     if not number_patern.fullmatch(pasword):
#         return (False, "Пароль не має цифр")
#     if not symbols_patern.fullmatch(pasword):
#         return (False, "Пароль не має символів")
#     return (True, "Password valid")
#
#
# while True:
#     password = input('Ввести пароль:')
#     pasword_result = check_pasword(password)
#     if pasword_result[0]:
#         print(pasword_result[1])
#         break
#     print(pasword_result[1])
