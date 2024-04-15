#1.Write a program to print the sum of integer values present in list.
l=input("Enter list Elements:")
list1=l.split(',')
list2=[]
for i in list1:
    if i.isdigit():
        list2.append(int(i))
total=0
for i in list2:
    total +=i
print('The Sum of the integer values present in the list is:',total)

#2.Write a program to find entered name is present in list of employees name or not.

l=input("Enter list Elements:")
list1=l.split(',')
print(list1)
name=input("Enter the name you want to check:")
if name in list1:
    print("Yes, Present")
else:
    print("Not Present")

#3.Write a program that accepts a list from user and print the alternate element of list.
l=input("Enter the list elements:")
l1=l.split(',')
print(l1)
print(l1[::2])

#4.Write a program that accepts a list from user.
#Your program should reverse the content of list and display it. Do not use reverse() method.
l=[]
n = int(input("How many elements you want in the List:"))
for i in range(n):
    el=input("Enter Element:")
    if el.isdigit():
        el=int(el)
        l.append(el)
    else:
        l.append(el)
print(l)
print(l[::-1])

#5.Find and display the largest number of a list without using built-in function max().
# Your program should ask the user to input values in list from keyboard.
l=[]
n = int(input("How many elements you want in the List:"))
for i in range(n):
    el=input("Enter Element:")
    if el.isdigit():
        el=int(el)
        l.append(el)
    else:
        l.append(el)
print(l)
maximum=0
for i in l:
    if maximum<i:
        maximum=i
print(maximum)

# 6.Write a program that rotates the element of a list
# so that the element at the first index moves to the second index, the element in the second index
# moves to the third index, etc., and the element in the last index moves to the first index.
# use slicing
l=[]
n = int(input("How many elements you want in the List:"))
for i in range(n):
    el=input("Enter Element:")
    if el.isdigit():
        el=int(el)
        l.append(el)
    else:
        l.append(el)
print(l)
nl=l[0:len(l)-1]
nl.insert(0,l[len(l)-1])
print(nl)

#type 2
l1 = input("Enter name in the list separated by , :")
list1 = l1.split(',')
for i in range(len(list1)):
    # convert each item to int type
    list1[i] = int(list1[i])
l = list1[-1:] + list1[:-1]
print(l)

# 7.Write a program that input a string and ask user to delete a given word from a string.
s=input("Enter your string:")
print(s)
l = s.split(' ')
d=input("Enter the word you want to delete from string:")
print(l)
l.remove(d)
print(' '.join(l))


# 8.Write a program with a function that accepts a string from keyboard and create a new string
# after converting character of each word capitalized. For instance,
# if the sentence is "stop and smell the roses." the output should be "Stop And Smell The Roses"
str=input("Enter your string here:")
print(str)
print(str.title())





