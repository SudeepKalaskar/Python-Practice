#1. WAP to print values from 1 to 10.
c=1
while c<=10:
    print(c)
    c+=1

#2. WAP to print values from 10 to 1.
c=10
while c>=1:
    print(c)
    c-=1

#3. WAP to print values from 5 to 15.
c=5
while c<16:
   print(c)
   c+=1

#4. WAP to print values from 1 to entered number.
num = int(input("Enter Number:"))
c=1
while c<=num:
    print(c)
    c+=1

#5. WAP to print entered name n number of times.
name=input("Enter Name:")
n = int(input("how many times you want to print your name:"))
c=1
while c <= n:
    print(c, name)
    c+=1

#6. WAP to print the table of 5.
c=5
while c<51:
    print(c)
    c+=5

#7. WAP to print the table of any entered number.
num = int(input("Enter Number:"))
c=num
while c<= (num*10):
    print(c)
    c+=num

#8. WAP to print the values between two entered number.
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
c=a
while c<b:
    print(c)
    c+=1
