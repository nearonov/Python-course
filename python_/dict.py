# my_motobike = {
#     'brand': 'Dukati',
#     'price': 25000,
#     'engine_vol': 1.2,
# }
#
# other_motobike = {
#     'engine_vol': 1.2,
#     'brand': 'Dukati',
#     'price': 25000,
# }
# print(my_motobike == other_motobike)
# # True
# print(id(my_motobike) == id(other_motobike))
# # False
# print(my_motobike['brand'])
# # Dukati

# Додавання та видалення ключа та значення

# my_motobike = {
#     'brand': 'Dukati',
#     'price': 25000,
#     'engine_vol': 1.2,
# }
# my_motobike['is_new'] = True
# print(my_motobike)
# #{'brand': 'Dukati', 'price': 25000, 'engine_vol': 1.2, 'is_new': True}
#
# del my_motobike['is_new']
# print(my_motobike)
# #{'brand': 'Dukati', 'price': 25000, 'engine_vol': 1.2}

# ДОСТУП ДО ЗНАЧЕННЯ ЕЛЕМЕНТА ЗА ДОПОМОГОЙ ЗМІННОЇ

# my_motobike = {
#     'brand': 'Dukati',
#     'price': 25000,
#     'engine_vol': 1.2,
# }
# key_name = 'brand'
# my_motobike[key_name] = 'BMW'
# print(my_motobike)
# # {'brand': 'BMW', 'price': 25000, 'engine_vol': 1.2}
#
# brand = 'java'
# price = 2000
# engine_vol = 1, 3
# other_motobike={
#     'brand':brand,
#     'price':price,
#     'engine_vol':engine_vol
# }
# print(other_motobike)
# #{'brand': 'java', 'price': 2000, 'engine_vol': (1, 3)}

# def dict(arg):
#     return arg
# arg=input('Ввести значення:')
#
# other_motobike={
#     'brand':dict(arg),
#
#
# }
# print(other_motobike)


# Довжина словника

# my_motobike = {
#     'brand': 'Dukati',
#     'price': 25000,
#     'engine_vol': 1.2,
# }
# print(len(my_motobike))#3
#
# #НЕ ІСНУЮЧИ КЮЧИ І МЕТОД get
# print(my_motobike.get('collection'))#None

# КОПІЯ СЛОВАРЯ

# my_disk = {}
# print(my_disk)
# my_disk['brand'] = 'Samsung'
# my_disk['price'] = 2500
#
# new_disk = my_disk.copy()
# new_disk['type'] = 'ssd'
# print(my_disk, 'id:', id(my_disk))
# print(new_disk, 'id:', id(new_disk))
# # {}
# # {'brand': 'Samsung', 'price': 2500} id: 2183576572672
# # {'brand': 'Samsung', 'price': 2500, 'type': 'ssd'} id: 2183577960128

# КОНВЕРТАЦИЯ СПИСКА В СЛОВНИК

# my_list = [['abs', 1], [True, 2]]
# my_dict = dict(my_list)
# print(my_dict)

#Практика

my_dict = {}
for n in range(3):
    key= input('Ввести ключ :')
    key_arg = input('Ввести значення ключ :')
    my_dict[key]= key_arg
print(my_dict)
# fourth = 4
# my_dict [4] = 'vbn'
# del my_dict [second]
# print(my_dict)
