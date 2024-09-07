from datetime import datetime, date, time, timedelta
import time

# my_date = date(2024, 8, 5)
# print(my_date) #2024-08-05
# print(my_date.isocalendar()) #(year=2024, week=32, weekday=1)
#
# my_time = time(23, 32, 00)
# print(my_time) #23:32:00
# print(my_time.max) #23:59:59.999999
# print(my_time.min) #00:00:00
# print(my_time.minute) #32
#

# Форматування дат

# my_date_time = datetime(2024, 8, 5, 23, 32, 00)
# print(my_date_time) #2024-08-05 23:32:00
# print(my_date_time.now().time()) #23:52:11.770478  час на компе
# print(my_date_time.strftime('%d-%b-%Y %H:%M:%S')) #05-Aug-2024 23:32:00

# data_str = '06/08/2024 21/50/32'
# convert_data = datetime.strptime(data_str, '%d/%m/%Y %H/%M/%S')
# print(convert_data)  # 2024-08-06 21:50:32
# print(convert_data + timedelta(days=100, hours=2))  # 2024-11-14 23:50:32

# my_time = time.ctime(20)
# print(my_time)  # Thu Jan  1 02:00:20 1970

# start_time = time.time()
# time.sleep(4)  # затримка в 4 сек.
# end_time=time.time()
# print(end_time - start_time) #4.001070261001587

start_time = time.time()
ran = list(range(10000000))
print(ran[1000])
end_time = time.time()
print("Час роботи ran :", end_time-start_time) #Час роботи ran : 0.42196130752563477
