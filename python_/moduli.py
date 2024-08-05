from function import *
from packet import other_modul,one_more_modul
import math

# print(f"__name__ = {__name__}")

#__name__ = function

func() #Функція відпрацювала!

print(math.pi) #3.141592653589793
print(math.pow(4,2)) #16

other_modul.my_fn()
print(one_more_modul.c)
one_more_modul.my_name('Hello!')

