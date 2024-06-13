# fruits = ['banana', 'lime', 'apple']
# quantities = [100, 200,50]
# fruits_quan_zip = zip(fruits,quantities)
# fruits_quan_list = list(fruits_quan_zip)
# print(fruits_quan_list)


# Конветація zip в dict.

fruits = ['banana', 'lime', 'apple']
quantities = [100, 200,50]
fruits_quan_zip = zip(fruits,quantities)
fruits_quan_list = dict(fruits_quan_zip)
print(fruits_quan_list)
