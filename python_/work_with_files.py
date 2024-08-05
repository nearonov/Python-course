from os import path
from pathlib import Path

# my_file = open('D:\python_kurs.txt', 'w')
# my_file.write("Привіт Євген 27.07.2024 р.\n")
# my_file.write("Я вивчаю Python.\n")
# my_file.close()
# #
# my_file = open('D:\python_kurs.txt').readline()
# #my_file.close()
#
# other_file = open('D:\eugen.txt', 'w')
# other_file .write("Документація та непідтримувані функції\n")
# other_file.close()
#
# other_file = open('D:\eugen.txt').read()
# #print(other_file)
# #other_file.close()
#
#
# print(open('D:\каб.УАРНЕТ.txt').read())

# print(path.abspath('.'))#C:\store-server\src\Python course\python_
# print(Path('.').absolute())#C:\store-server\src\Python course\python_
# print(Path('decarator.py').is_file())#True
#
# for f in Path('.').iterdir():
#     print(f,end=" ") #classes_objects.py  decarator.py  dict.py  error_handling.py  for_in.py  function.py  if.py  json_.py  lesson_1.py  list.py  logical_operators.py

swd = Path('.').absolute()
a = Path('D:/').joinpath('nearonov')
if not a.exists():
    a.mkdir()  # создаємо папку nearonov , а потім викдючаємо функцію mkdir()
print(swd)  # C:\store-server\src\Python course\python_
print(a)  # D:\nearonov
print(a.exists())  # True перевыряэмо є такий файл 1.txt') на комп.

# Создаємо файл в папці D:\nearonov\1.txt
# my_file = open('D:/nearonov/1.txt', 'w')
# my_file.write('Увага! Класифікація визначає приблизний вік рослини вказаний.\n')
# my_file.write('постачальником, а не ії фізичні розміри. S/S - seedling size / сіянець, NB/S -\n')
# my_file.close()

# Другий спосіб

with open('D:/nearonov/1.txt', 'w') as my_file:
    my_file.write('Увага! Класифікація визначає приблизний вік рослини вказаний.\n')
    my_file.write('постачальником, а не ії фізичні розміри. S/S - seedling size / сіянець, NB/S -\n')
    my_file.write('near bluming size / молода рослина, яка не досягла віку цвітіння, B/S -\n')
# my_file = open('D:/nearonov/1.txt').read()
with open('D:/nearonov/1.txt') as my_file:
    # for line in my_file:
    while True:
        line = my_file.readline()
        print(line)
        if not line:
            break

with open('D:/nearonov/2.txt', 'w') as other_file:
    other_file.write("Amazon Web Services — найбільший і найрозвиненіший провайдер хмарних послуг.\n ")

with open('D:/nearonov/2.txt') as other_file:
    print(other_file.read())

# f = Path('D:/nearonov/2.txt')
# if f.exists():
#     f.unlink()

# if a.exists(): # Видалення папки nearonov
#     a.rmdir()

# ---------------------------------------------------------------
# Завдання
# ------------------------------------------------------------------
#1. Создати папку files
#2. Добавити в папку два файла first.txt  second.txt
#   записати в них по 3 строкию
#3. Прочитати строки першого файла
#4. Прочитати строки другого файла одна за другой великими буквами
#5. Удалити оба файла
#6. Удалити папку files

f = Path('D:/').joinpath('files')
if not f.exists():
    f.mkdir()
with open('D:/files/first.txt', 'w') as info:
    info.write('Cattleya forbesii - один из наиболее распространенных видов двулистных\n'.upper())
    info.write('каттлей. Эта орхидея произратает в Бразилии в штатах Рио-де-Жанейро,\n'.upper())
    info.write('Санта Катарина и Парана, на высотах до 200 метров над уровнем моря.\n'.upper())
with open('D:/files/first.txt') as info:
    print(info.read())
swd = Path('D:/files/first.txt')
if swd.exists():
    swd.unlink()

with open('D:/files/second.txt', 'w') as loock:
    lists = ['Cattleya forbesii - эпифит или литофит.\n'.upper(),
            'У нее тонкие псевдобульбы до 20 см высотой.\n'.upper()
            ]
    for list in lists:
        loock.write(list)
    # loock.write('Cattleya forbesii - эпифит или литофит.\n'.upper())
    # loock.write('У нее тонкие псевдобульбы до 20 см высотой.\n'.upper())

with open('D:/files/second.txt') as loock:
    while True:
        s = loock.readline()
        print(s.strip()) #strip уберає побіди і переходи на нову стоку
        if not s:
            break
zxc = Path('D:/files/second.txt')
if zxc.exists():
    zxc.unlink()

if f.exists():
    f.rmdir()


