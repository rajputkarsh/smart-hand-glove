import csv
import urllib.request


for i in range(20):
    with urllib.request.urlopen('http://192.168.1.72') as x:
        data = x.read()
        data = data.decode('utf-8')
        csv_row = data.split()
    csv_row.append('5')
    with open(r'C:\Users\Admin\Documents\nodemcu_dataset.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(csv_row)
print("50 rows added !!!")
