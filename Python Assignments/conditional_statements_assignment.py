# 1. WAP to find greater number between two entered number.
a= float(input("Enter number 1:"))
b= float(input("Enter number 2:"))

if a>b: #12 > 12-->F
    print(a,"is greater than",b)
elif a==b:
    print(a,"is equal to", b)
else:
    print(b,"is greater than",a)


# 2. WAP to find to entered numbers are equal or not
a1 = int(input("Enter number 1:"))
a2 = int(input("Enter number 2:"))
if (a1 == a2):
     print(a1,"is equal to",a2)
else:
     print(a2,"is not equal to",a1)


# 3. WAP to find entered numbers are positive or negative.
a= float(input("Enter number:"))
if (a>0):
    print(a,"is a positive number")
else:
    print(a,"is a negative number")

# 4. WAP to find entered number is even or odd.
a= int(input("Enter number:"))
if (a%2==0):
    print(a,"is an even number")
else:
    print(a,"is a odd number")

# 5. WAP to find the entered character is vowel or not.
ch = input("Enter Character:")
if ch=='a':
    print("Yes it is vowel")
elif ch=='e':
    print("Yes it is vowel")
elif ch=='i':
    print("Yes it is vowel")
elif ch=='o':
    print("Yes it is vowel")
elif ch=='u':
    print("Yes it is vowel")
else:
    print("It is not a vowel")

# 6. WAP to print the days of the week according to the entered day number.
# Day 1 = Monday, Day 7 = Sunday
print("For days name please enter a number between 1 to 7:")
day = int(input("Enter day number:"))
if day==int(1):
    print("Entered day is Monday")
elif day==int(2):
    print("Entered day is Tuesday")
elif day==int(3):
    print("Entered day is Wednesday")
elif day==int(4):
    print("Entered day is Thursday")
elif day==int(5):
    print("Entered day is Friday")
elif day==int(6):
    print("Entered day is Saturday")
elif day==int(7):
    print("Entered day is Sunday")
else:
    print("Please enter a valid day number, Thankyou")

# 7. WAP to perform arithmetic operations between two integers values according to the operator entered by user.
a= int(input("Enter 1st integer number:"))
b= int(input("Enter 2nd integer number:"))
op= input("Enter arithmetic operator:")
if op=='+':
    print("Addition of",a,"and",b,"is",a+b)
elif op=='-':
    print("Subtraction of",a,"and",b,"is",a-b)
elif op=='*':
    print("Multiplication of", a,"and",b,"is",a*b)
elif op=='/':
    print("Division of",a,"and",b,"is",a/b)
elif op=='//':
    print("Floor division of",a,"and",b,"is",a//b)
elif op=='%':
    print("Remainder of",a,"and",b,"is",a%b)
else:
    print("You have entered a invalid operator")




