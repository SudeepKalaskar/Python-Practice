"""l1=[90,23,89,12,78]
print(min(l1))
print(max(l1))
print(sum(l1))"""
#print(abs(-78))
#print(pow(2,4))

#import math
"""#print(math.sqrt(16))
#print(math.pi)
print(math.ceil(5.2))
print(math.floor(5.2))"""

import datetime

"""d=datetime.datetime.now()
#d=datetime.datetime(2022,11,21,10,45)
print(d.strftime("%y%a%B"))"""

#user will enter name before that gm,gf,ge,gn should come before name
"""d=datetime.datetime.now()
d1=d.strftime("%H")
#print(d.strftime("%d %m %Y"))
name = input('enter name')
if int(d1) < 5:
    print('Good Night', name)
elif int(d1) >5 and int(d1) <12:
    print('Good Morning', name)
elif int(d1) > 12 and int(d1) < 17:
    print('Good Afternoon', name)
elif int(d1) > 17 and int(d1) < 23:
    print('Good Evening', name)"""

#os
import os
"""print(os.getcwd())
print(os.listdir("C:\\"))"""
#os.mkdir("sssss")
#os.mkdir("E:\\Python\\sss")
#os.rename("sssss","kkkkk")
#os.rename("E:\\Python\\sss","E:\\Python\\$$$")
#os.rmdir("kkkkk")
"""f=open("mmm.txt","a")
f.write("This is appended data\n")
f.write("This is rockstar\n")
f.write("This is third rockstarcool\n")"""
"""f=open("mmm.txt","r")
#print(f.read())
#print(f.read(4))
print(f.readline())
print(f.readline())"""

#wap creating a text file containing 10 lines.read only starting 4 lines
"""f=open("new file.txt","a")
f.write("This is appended data\n")
f.write("This is rockstar\n")
f.write("This is third rockstarcool\n")
f.write("This is fourth rockstarcool\n")
f.write("This is fifth rockstarcool\n")
f.write("This is sixth rockstarcool\n")
f.write("This is seventh rockstarcool\n")
f.write("This is eight rockstarcool\n")
f.write("This is third nine rockstarcool\n")
f.write("This is ten rockstarcool\n")
f=open("new file.txt","r")
#print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())"""

#wap reading an existing file.
"""count no. of spaces
count no. of characters
count no. of digits
count no.of special characters"""

"""f=open('new file.txt','r')
dcount=0
spcount=0
acount=0
splcount=0
for t in f.read():
    if t.isalpha():
        acount=acount+1
print(acount)"""

#lambda function
"""def add(a,b):
    return(a+b)"""
"""add=lambda a,b:a+b
x=10
y=20
s=add(x,y)
print(s)"""

#create a labmda function to calculate area of rectangle

"""add=lambda l,w:l*w
x=2
y=5
area=add(x,y)
print(area)"""













