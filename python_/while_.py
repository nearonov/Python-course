# from random import randint
#
# random_num = randint(1, 5)
# while True:
#     num = int(input("Ввести  число від 1 до 5 :"))
#     if num!=random_num:
#         print("Не вгадав спробуй ще!")
#         continue
#     print("Ви вгадали число", random_num)
#     break


info = 'yes'
while info!='no':
    try:
        num_one = float(input("Введіть перше число:"))
        num_two = float(input("Введіть друге число:"))
        print("Результат ділення :", num_one/num_two)
    except ValueError as e:
        print(e)
        print("Ви ввели не цифру")
        continue
    except ZeroDivisionError as e:
        print(e)
        print("На нуль ділить не можна!!!")
        continue
    info = input("Якщо ви хочите продовжити введіть yes, як що ні то no :")
    if info=='no':
        break
print("Закінчення роботи програми.")

# while True:
#     try:
#         num_one = float(input("Введіть перше число:"))
#         num_two = float(input("Введіть друге число:"))
#         print("Результат ділення :", num_one/num_two)
#     except ValueError as e:
#         print(e)
#         print("Ви ввели не цифру")
#         continue
#     except ZeroDivisionError as e:
#         print(e)
#         print("На нуль ділить не можна!!!")
#         continue
#     info = input("Якщо ви хочите продовжити введіть yes, як що ні то no :")
#     if info == 'no':
#          break
# print("Закінчення роботи програми.")



