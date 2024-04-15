# 1. Write a program to check entered character is vowel or not?
ch = input("Enter character:")
if ch =='a' or ch =='e' or ch =='i' or ch =='o' or ch =='u' or ch =='A' or ch =='E' or ch =='I' or ch =='O' or ch =='U':
    print("Yes it is vowel")
else:
    print("It is not a vowel")

# 2. Write a program to print weekday if entered day number is 1,2,3,4,5 and print weekend if entered day is 6 or 7.and invalid day if value not between 1 to 7.
print("Please enter day number between 1 to 7")
day = input("Enter day number:")
if day == '1' or day == '2' or day == '3' or day == '4' or day == '5':
    print("Entered day number is a weekday")
elif day == '6' or day == '7':
    print("Entered day is weekend")
else:
    print("Enter a valid day number")

# 3.Write a program to find greatest among three numbers.
# type 1: static values
a=10
b=5
c=50
if a>b and a>c:
    print("Yes", a, "is greatest")
elif b>a and b>c:
    print("Yes", b, "is greatest")
else:
    print("Yes", c, "is greatest")

#type 2: taking input from user
a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter number 3:"))
if a>b and a>c:
    print("Yes", a, "is greatest")
elif b>a and b>c:
    print("Yes", b, "is greatest")
else:
    print("Yes", c, "is greatest")

# 4. A candidate is recruited based on following criteria:
# If male, age should be above 30 yrs and height above 160.
# If female, age should be above 25yrs and height above 155.

print("Please enter M or m for male and F or f for female")
gen = input("Enter your gender:")
age = int(input("Enter your Age in years:"))
ht = float(input("Enter your Height in cm:"))
if gen=='M'or'm' and age>=30 and ht>=160:
    print("You are selected")
elif gen=='F'or'f' and age>=25 and ht>=155:
    print("You are selected")
else:
    print("Sorry, You are not selected")


