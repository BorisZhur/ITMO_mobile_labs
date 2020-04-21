import csv
import matplotlib.pyplot as plt
from datetime import datetime

addr="192.168.250.1"
kb = 0
x=[]
y=[]
with open('data3.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row['sa'] == addr) | (row['da'] == addr):
            kb = kb + int(row['ibyt'])
            x.append(datetime.strptime(row['ts'],"%Y-%m-%d %H:%M:%S"))
            y.append(kb/1048576)
# print(x)
# print(y)
k=0.5
sum=0.5
sum=sum-0.5
mb=kb/1048576
# print(mb)
while mb>=500:
    sum=sum+(500*k)
    k=k+0.5
    mb=mb-500

sum=sum+(mb*k)
print(sum)
plt.plot(sorted(x),y)
plt.title("Traffic(time)")
plt.xlabel("time")
plt.ylabel("MegaBytes")
plt.show()


