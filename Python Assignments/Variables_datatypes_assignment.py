# 1. WAP to print hello
print("Hello")

# 2. WAP to print addition of two numbers
# (1)
a = 25
b = 75
print("Addition of a and b is", a+b)

# (2)
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
print("Addition of", a,"and", b,"is", a+b)

# 3. WAP to calculate area of rectangle
l = 6
b = 4
print("Area of rectangle is", l*b)

# (2)
l = int(input("Enter length of rectangle:"))
b = int(input("Enter breadth of rectangle:"))
print("Area of rectangle is", l*b)

# 4. WAP to calculate simple interest taking input from user
p = int(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest in percentage:"))
t = float(input("Enter the time in years:"))
i = (p*r*t)/100
print("The simple interest will be",i)

# 5. WAP to calculate the cube of entered number
x = int(input("Enter the number:"))
print("The cube of entered number is", x**3)

# 6. WAP to take any employee details and display it
name = input("Enter your name:")
date_of_joining = input("Enter your date of joining:")
dept = input("Enter your department:")
ph_no = int(input("Enter your phone number:"))
salary = float(input("Enter your salary in LPA:"))
print("Employee Details")
print("Employee Name:", name)
print("Date of Joining:", date_of_joining)
print("Enter Department:", dept)
print("Enter your Phone Number:", ph_no)
print("Enter your salary in LPA:", salary)

# 7. WAP to take a number from user decrement the value by 3
n = int(input("Enter the number:"))
n -= 3
print("The number after decrement by 3 will be:", n)

