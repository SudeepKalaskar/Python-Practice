"""name=Sudeep
print (type(name))"""

"""st="Hello"
#print(st)
print(st[0])
print(st[2])
print(st[3])
print(st[-2])
print(st[-4])"""

#[start:stop:step]

"""lan="python class"
print(lan[2:6])
print(lan[:7])
print(lan[3:])
print(lan[3:11:1])
print(lan[::-2])"""

#string operators
#+
#+concatenation operator
"""firstname=input("enter firstname")
lastname=input("enter lastname")
fullname=firstname+" "+lastname
print(fullname)
#*repeation operator
ss=firstname+" "
kk=ss*5
print(kk)"""

#in/notin
"""language="python programming language"
#print("py2thon" in language)
if "python" in language:
    print("present")
else:
    print("no")"""

#wap taking address from candidate.if address contains
#pune then the candidate is eligible for interview or not?
"""address=("shivajinagar pune")
print("pune" in address)
if "pune" in address:
    print("eligible")
else:
    print("not")"""

"""l="python"
#for loop
for i in l:
    print(i)"""

"""l="python"
count=0
while count<len(l):
    print(l[count])
    count=count+1"""

#traverse a string in reverse order
"""l="python"
count=len(l)-1
while count>=0:
    print(l[count])
    count=count-1"""

#string manipulation functions
"""l="python language class"
#print(l.count('a'))
#print(l.find('ak'))
#print(l.index('am'))"""

#string manipulation functions
"""l="python language class"
#m=l.title()
#m=l.capitalize()
print(l)
print(m)"""

#string manipulation functions
"""l="python language class"
print(l.upper())
print(l.lower())
print(l.islower())
print(l.isupper())"""

#wap to traverse every alternate character from the entered string
"""a=input("enter a string:")
b=""
for i in range(0,len(a),2):
    b+=a[i]
print("alternate characters:",b)"""
#wap to find how many times the enetered character is present in entered string
"""s="python programing"
print(s.count('p'))"""
#wap to find the position of entered character in entered string
"""j="python class"
print(j.find('h'))"""
#wap to find how many lowercase letters are present in entered string
"""name=input("enter your fullname")
count=0
for n in name:
    if n.islower():
        count=count+1
print(count)"""

#replace function
"""l="python language is my fav language python python"
m=l.replace("python","java",2)
print(m)"""

#split function
"""l="python language i-s my fav- lang-uage pyt-hon pyt-hon"
m=l.split('-',2)
print(m)"""

"""data="      "
print(data.isdigit())
print(data.isalnum())
print(data.isalpha())
print(data.isspace())
if data.isspace():
    print("yes")
else:
    print("no")"""

#user will enter address
#count no. of digits
#no. of alphabets
#no. of spaces
#no. of special character

"""add=input("enter address")
acount=0
dcount=0
spcount=0
slcount=0
for a in add:
    if a.isspace():
        spcount=spcount+1
    elif a.isdigit():
        dcount=dcount+1
    elif a.isalpha():
        acount=acount+1
    else:
        slcount=slcount+1
print("spaces",spcount)
print("alphabets",acount)
print("digits",dcount)
print("special",slcount)"""

#Write a program to print the number of vowels present in entered string.
"""vovels=input("enter vowels")
x=0
for a in vovels:
    if a.isalpha():
        x=x+1
    else:
        print("invalid")
print("vowels",x)"""

#list function
"""l1=[]
l2=[89,90]
l3=[40,90,72,90]
l4=[79,80,75.3]
print(l4)
#or print(type(l4))"""

# + * in not in
#1)create two list l1,l2 .conactenate two list
"""l1=[10,15,17]
l2=[19,20,25]
a=l1+l2
print(a)"""
#2)create one list.repeat the list 3 times
"""l1=[15,20,25]
a=l1*3
print(a)"""
#3)wap to find the city pune is present in list of 5 cities.
"""a = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Pune"]
b = "Pune"
if b in a:
    print("(b) is present in the list of a")
else:
    print("(b) is not present in the list of a")"""

#1)wap to find how many times the entered name is
#present in list of 8 employees names
"""emp=["rock","abel","akiston","rushi","rock","barley","rock","romey"]
n=input("Enter the name")
print(emp.count(n))"""

#2)wap to find the first value of two lists are same or not?
"""l1=[1,2,3,4]
l2=[1,7,5,6]
n=input("enter value")
if l1[0]==l2[0]:
    print("same")
else:
    print("not same")"""

"""l1=[90,78,90,67,45]
for t in l1:
    print(t)"""

"""c=0
while c<len(l1):
    print(l1[c])
    c=c+1"""

#1)wap to find how many times the entered name is
#present in list of 8 employees names without using count()
"""names=["rock","abel","akiston","rushi","rock"]
name=input("Enter name")
c=0
for n in names:
    if n==name:
        c=c+1
print(c)"""

#min,max,sum,len functions
"""l1=[90,67,12,78,45]
print(min(l1))
print(max(l1))
print(sum(l1))
print(len(l1))"""

#desending true, ascending false
"""l1=[90,67,12,78,45]
l1.sort(reverse=True)
print(l1)
#print(l1.reverse())
#print(l1)"""

"""l1=[34,89]
l2=[90,78,56]
print(l1)
#extend to combine values
l1.extend(l2)
print(l1)
#insert to add values in between
#l1.insert(1,900)
#print(l1)
#append add value to list
#l1.append(10)
#print(l1)"""

#slicing and updation
"""l1=[34,89,56,89,12]
print(l1)
#l1[1]=900
l1[1:4]=[23,54,78]
print(l1)"""

#delete function
"""l1=[34,89,56,89,12,34]
print(l1)
#l1.clear()
#l1.remove(34)
#l1.pop(2)#index
#del l1[2]#index
del l1
print(l1)"""

#creating a list user will enter 5 marks
"""l1=[]
print("Enter 5 marks")
for t in range(5):
    l1.append(int(input()))
print(l1)"""



























