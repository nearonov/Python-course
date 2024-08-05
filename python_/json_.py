import json

# Конвертація json в словник

# json_str = '{"id":123, "Eugene":55, "asd":{"Nataliy":49, "zxc":"Hello!"}}'
# s = json.loads(json_str)
# print(type(s))#<class 'dict'>
# print(s["id"])#123
# print(s)#{'id': 123, 'Eugene': 55, 'asd': {'Nataliy': 49, 'zxc': 'Hello!'}}
# print(s['asd']['Nataliy'])#49
#
# # Конвертація словник в  json
#
# my_json = json.dumps(s, indent=2)
# print(my_json)# {"id": 123, "Eugene": 55, "asd": {"Nataliy": 49, "zxc": "Hello!"}}
# print(type(my_json))#<class 'str'>
# # Конвертація масива(json object)  в  список
#
# json_array = '[34, 56, 67]'
#
# f=json.loads(json_array)
# print(f)# [34, 56, 67]

name = dict(first='Bob', last ='Smith')
rec = dict(name = name, job = ['dev', 'mgr'], age = 40.5)
# dict->json
json_dict = json.dumps(rec)
print(rec, type(rec))#{'name': {'first': 'Bob', 'last': 'Smith'},
# 'job': ['dev', 'mgr'], 'age': 40.5} <class 'dict'>

print(json_dict, type(json_dict))#{"name": {"first": "Bob",
# "last": "Smith"}, "job": ["dev", "mgr"], "age": 40.5} <class 'str'>

# json->dict
dict_json = json.loads(json_dict)
print(dict_json, type(dict_json))#{'name': {'first': 'Bob',
# 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5} <class 'dict'>

