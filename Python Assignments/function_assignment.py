# 1.Write a Python function to find the Max of three numbers.
# def maximum(a,b,c):
#     if a>b and a>c:
#         print(a,"is maximum")
#     elif b>c and b>a:
#         print(b,"is maximum")
#     else:
#         print(c,'is maximum')
# maximum(10,20,30)
# maximum(25,15,10)
#
# # 2.Write a Python function to sum all the numbers in a list.
# def add(*n):
#     s=0
#     for i in n:
#         s=s+i
#     print(s)
# add(*[1,2,3,4,5])
#
# # 3.Write a Python function to multiply all the numbers in a list.
# def product(*n):
#     p=1
#     for i in n:
#         p=p*i
#     print(p)
# product(*[3,4,5])
#
# # 4.Write a Python program to reverse a string.
# def rev(str):
#     print(str[::-1])
# rev("hello")
#
# # 5.Write a Python function to check whether a number falls in a given range.
# def chk(a,b,x):
#     for i in range(a,b):
#         if i==x:
#             print('Present')
#             break
#     else:
#         print('Not Present')
# chk(10,20,25)
# chk(11,21,18)
#
#
# # 6.Write a Python function that accepts a string and calculate
# # the number of upper case letters and lower case letters.
#
# def cal(str1):
#     c = 0
#     s = 0
#     for i in str1:
#         if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#             c+=1
#         elif i in 'abcdefghijklmnopqrstuvwxyz':
#             s+=1
#         else:
#             pass
#     print("The number of upper case letters in the string is:", c)
#     print("The number of lower case letters in the string is:", s)
# cal('Hello We Learn Python')
# cal('My Name is JOHN')

# type 2
def cal2(str3):
    c=0
    s=0
    for i in str3:
        if i.isupper():
            c+=1
        elif i.islower():
            s+=1
        else:
            pass
    print("The number of upper case letters in the string is:", c)
    print("The number of lower case letters in the string is:", s)
cal2('Hello We Learn Python')
cal2('My Name is JOHN')


