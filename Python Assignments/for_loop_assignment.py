# #1.WAP to print the factorial of entered number.
# n = int(input("Enter Number:"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(fact)
#
# #2.WAP to print sum of first five positive integer numbers.
# #type 1
# sum = 0
# for i in range(1,6):
#     sum = sum+i
# print(sum)
#
# #type 2 taking input from user
# a = int(input("Enter number 1:"))
# b = int(input("Enter number 2:"))
# sum = 0
# for i in range(a,b+1):
#     sum = sum+i
# print(sum)
#
# #3.WAP to find entered number is prime or not.
# n= int(input("Enter any number:"))
# for i in range(2,n):
#     if n%i ==0:
#         print('not prime')
#         break
#     else:
#         pass
# else:
#     print('prime')
#
# # WAP to print all the prime numbers between 1 and 100.
# for i in range(1,101):
#     count=0
#     for j in range(1,i+1):
#         if (i%j==0):
#             count=count+1
#     if count==2:
#         print(i,end=' ')
#
#
# #4.WAP to print all the even numbers between 1 and 20.
# #type 1
# for i in range(1,21):
#     if i%2==0:
#         print(i)