from zipfile import ZipFile
from pathlib import Path

# fruits = ['banana', 'lime', 'apple']
# quantities = [100, 200,50]
# fruits_quan_zip = zip(fruits,quantities)
# fruits_quan_list = list(fruits_quan_zip)
# print(fruits_quan_list)
#[('banana', 100), ('lime', 200), ('apple', 50)]
import copy

# Конвертація zip в dict.

# fruits = ['banana', 'lime', 'apple']
# quantities = [100, 200,50]
# fruits_quan_zip = zip(fruits,quantities)
# fruits_quan_list = dict(fruits_quan_zip)
# print(fruits_quan_list)
#{'banana': 100, 'lime': 200, 'apple': 50}

# car = ('BMV', 'Wolsvagen', 'Audi')
# price = (20000,15000,18000)
# car_pr_zip = zip(car,price)
# car_pr_zip_copy = zip(car,price)
# car_pr_dict = dict(car_pr_zip)
# car_pr_list = list(car_pr_zip_copy)
# print(car_pr_dict)
# print(car_pr_list)



# a = Path("D:/").joinpath("my_files")
# if not a.exists():
#     a.mkdir()
# with open("D:/my_files/first.txt",'w') as my_file:
#     my_file.write("This is  first file")
# with open("D:/my_files/second.txt",'w') as my_file:
#     my_file.write("This is  second file")
#За коментуєм і прцюєм далі з first.txt і second.txt

with ZipFile('D:/my_files.zip',mode='w')as my_zip_file:#відкриваем файл my_files.zipв режиме 'w' запису
    for file in Path("D:/my_files").iterdir():
        print(file)#D:\my_files\first.txt D:\my_files\second.txt
        my_zip_file.write(file) # додаємо first.txt і second.txt в архів

#Распаковка zip архіва
with ZipFile("D:/my_files.zip") as my_files_zip:
    #my_files_zip.extractall("D:/my_files_unzip")
    print(my_files_zip.infolist())

