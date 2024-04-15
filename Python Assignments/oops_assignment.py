#1.Write a python program using class which contains two variables of type integer.
#Create and initialize the object using parameterized constructor.
#Write a method to display maximum from given two numbers for all objects.
# class Maximum:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#         print('This is Maximum of given numbers class')
#     def get_max(self):
#
#         if self.x>self.y:
#             print(self.x,'is greater than',self.y)
#         elif self.y>self.x:
#             print(self.y,'is greater than',self.x)
#         else:
#             print('Both the numbers are equal')
#
# m1=Maximum(10,15)
# m1.get_max()
#
# m2=Maximum(100,100)
# m2.get_max()

#2.Write a program to perform all the arithmetic operations between two numbers.
# class Am_ops:
#     def __init__(self,p,q):
#         self.p=p
#         self.q=q
#         print("This is Arithmetic operations class")
#     def addition(self):
#         ad=self.p+self.q
#         print("The addition of entered numbers is:",ad)
#     def subtraction(self):
#         if self.p>=self.q:
#             sb=self.p-self.q
#             print("The subtraction of entered numbers is:",sb)
#         elif self.p<self.q:
#             sb=self.q-self.p
#             print("The subtraction of entered numbers is:", sb)
#
#     def multiplication(self):
#         ml=self.p*self.q
#         print("The multiplication of entered numbers is:", ml)
#
#     def division(self):
#         if self.p>=self.q:
#             dv=self.p/self.q
#             print("The division of entered numbers is:", dv)
#         else:
#             dv=self.q/self.p
#             print("The division of entered numbers is:", dv)
#
#     def square(self):
#         sq1=self.p**2
#         sq2=self.q**2
#         print(f"The square of first entered number is {sq1} and of second entered number is {sq2}")
# n1=Am_ops(25,10)
# n1.addition()
# n1.subtraction()
# n1.multiplication()
# n1.division()
# n1.square()
# n1.__init__(12,12)

# type-2
# class AMops:
#     def operations(self,a,b):
#         print("Addition is:",a+b)
#         print("subtraction is:",a-b)
#         print("Multiplication is:",a*b)
#         print("division is:",a/b)
#         print("square are :",a**2,",",b**2)
#         print("remainder is :",a%b)
# n=AMops()
# n.operations(16,6)

#3.Write a program to find the records of students having greater marks.
# marks={"john":{"maths":87,"physics":79,"chemistry":65,"biology":91},
#        "alex":{"maths":75,"physics":67,"chemistry":51,"biology":87},
#        "nita":{"maths":61,"physics":58,"chemistry":90,"biology":74},
#        "lily":{"maths":59,"physics":81,"chemistry":71,"biology":54}}

# st_marks={"john":87,"alex":75,"nita":61,"lily":59}
# class students:
#     def get_max_m(self):
#         m_max=max(st_marks.values())
#         print(st_marks.values())
#         print("maximum marks in maths is:",m_max)
# p=students()
# p.get_max_m()



# Class work assignment
# parent/superclass shape --> method(area)
# circle(area) --> area() (must create constructor)
# rectangle(shape) --> area constructor l*w -->l*l
# square(rectangle) --> find square of any number i.e. takes vale of 'l' from rectangle class
# use super() method to call rectangle constructor and also call area method of constructor.

import math
class Shape:
    def area(self):
        print("This is area method of Shape class")

class Circle(Shape):
    def __init__(self,rad):
        super().area()
        self.rad=rad
    def area(self):
        ar_c=math.pi*self.rad**2
        print("The area of circle is:",ar_c)
class Rectangle(Shape):
    def __init__(self,l,b):
        super().area()
        self.l=l
        self.b=b
    def area(self):
        ar_r=self.l*self.b
        print("The area of the rectangle is:",ar_r)
class Square(Rectangle):
    def __init__(self,l):
        super().__init__(self,l)
        self.l=l


    def area(self):
         super().area()


area1=Circle(7)
area1.area()

area2=Rectangle(10,5)
area2.area()

area3=Square(6)
area3.area()