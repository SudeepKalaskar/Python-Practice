"""a=10
b=20
print("before")
try:
 c=a/b

except ZeroDivisionError as e:
    print("denominator can not be zero")
else:
    print(c)
finally:
    print("default code")
print("after")"""

"""l1=[9,8,3]
print(l1[12])
f1=open("gefggf.txt")"""
"""a=int(input("Enter first number"))
b=input("Enter second number")
print(a/b)"""


"""marks = int(input("enter your marks"))
try:
    if marks > 100:
        raise ValueError

    else:
        print(marks)
except ValueError:
    print("marks can not be greter than 100")"""

#wap taking age from user and raise ValueError if age is less than 18
"""try:
    age = int(input("Enter your age"))
    if age < 18:
        raise ValueError("Age must be 18 or older")
    else:
        print("You are eligible")
except ValueError as v:
    print(v)"""


