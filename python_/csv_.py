import csv

with open('D:/file.csv', 'w') as test_csv:
    writer = csv.writer(test_csv)
    writer.writerow(['id', 'name', 'comment_qty'])
    writer.writerow([5040, 'Eugene', 20])
    writer.writerow([6040, 'Nataliy', 50])
    writer.writerow([5040, 'Bogdan', 90])

with open('D:/file.csv')as test_csv:
    reader = csv.reader(test_csv)
    for element in reader:
        print(element)
