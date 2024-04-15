#1.Write a Python script to check whether a given key already exists in a dictionary.
#type 1
emp_details={'name':'john','dept':'IT','sal':45000,'hire_date':'17-04-2023'}
k=input('Enter the key ,you want to check:')

if k in emp_details:
    print('Yes,Exist')
else:
    print('Not Exist')

# type 2
emp_details={'name':'john','dept':'IT','sal':45000,'hire_date':'17-04-2023'}
j="mobile_number"
if j in emp_details:
    print('Yes exist')
else:
    print('Not exist')

# type 3
n = int(input('how many elements you want into dict:'))
emp={}
for i in range(n):
    key=input('Enter key:')
    value=input('Enter value:')
    emp[key]=value
print(emp)
k=input('Enter the key ,you want to check:')

if k in emp:
    print('Yes,Exist')
else:
    print('Not Exist')


# 2.Write a Python program to sum all the items in a dictionary.
s={'a':10,'b':15,'c':25,'d':20}
l=list(s.values())
print(l)
sum=0  # here we can use the function sum() also # print(sum(l))
for i in l:
    sum=sum+i
print(sum)


# 3.Write a Python program to multiply all the items in a dictionary.
s={'a':5,'b':8,'c':10,'d':3}
l=list(s.values())
print(l)
product=1
for i in l:
    product=product*i
print(product)


# 4.Write a Python program to sort a given dictionary by key.
#type 1
d={'banana':80,'apple':100,'mango':200,'guava':150}
print(d.keys())
nl=list(d.keys())
nl.sort()
print(nl)
d1={i:d[i] for i in nl}
print(d1)

#type 2
d={'banana':80,'apple':100,'mango':200,'guava':150}
print(d.keys())
nl=list(d.keys())
n2=list(d.values())
nl.sort()
print(nl)
print(n2)
vl =[]
for i in nl:
    vl.append(d[i])
print("dict",d)
print("key",nl)
print("values",vl)
d = dict(zip(nl,vl))
print("sorted dict:",d)



# 5.Write a Python program to get the maximum and minimum value in a dictionary.
# type 1
s={'a':10,'b':15,'c':25,'d':20}
l=list(s.values())
print(l)
maximum=0
for i in l:
    if maximum<i:
        maximum=i
print('The maximum value in the dictionary is:',maximum)

minimum=l[0]
for j in l:
    if j<minimum:
        j= minimum
print("The minimum value in the dictionary is:",minimum)

#type 2
numbers = {'a':'10', 'b':'20', 'c':'30', 'd':'50'}
n = numbers.values()
print(n)
maximum = max(n)
minimum = min(n)
print("Maximum value in dictionary is: ",maximum)
print("Minimum value in dictionary is:", minimum)

