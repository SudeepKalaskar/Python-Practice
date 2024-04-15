"""class Student:
    name="abc"
    age=12
    city="pune"
    def show(self):
        print(self.name,self.age,self.city)
s1=Student()
s2=Student()
s3=Student()
s1.show()
s2.show()
s3.show()"""

"""class Student:
    def __init__(self,rollno,name,city):#parameterized
        self.rollno=rollno
        self.name=name
        self.city=city
    def show(self):
        print(self.rollno,self.name,self.city)


s1=Student(101,"abc","pune")  #constructor implicitly
s2=Student(102,"pqr","nashik")
s3=Student(103,"hhh","mumbai")
s1.show()
s2.show()
s3.show()"""

#single inheritance
"""class parent:
    surname="abc"
class Child (parent):
    name="nnn"
    def show(self):
        print(self.name,self.surname)
c1=Child()
c1.show()"""

#Multilevel inheritance
"""class GP:
    surname="aaa"
class Parent(GP):
    middlename="ttt"
class Child(Parent):
    name="kkk"
    def display(self):
        print(self.name,self.middlename,self.surname)
c1=Child()
c1.display()"""

#hierarichal-one base class more than one child class
"""class Shape:
    def draw(self):
        print("will draw shape")
class Circle(Shape):
    pass
class Rectangle(Shape):
    pass
class Square(Shape):
    pass
c1=Circle()
r1=Rectangle()
s1=Square()
c1.draw()
r1.draw()
s1.draw()"""

"""class Shape:
    def draw(self):
        print("will draw shape")
class Circle(Shape):
    def draw(self):
        print("will draw Circle")
class Rectangle(Shape):
    def draw(self):
        print("will draw Rectangle")
class Square(Shape):
    def draw(self):
        print("will draw Square")
c1=Circle()
r1=Rectangle()
s1=Square()
c1.draw()
r1.draw()
s1.draw()"""

#multiple inheritance - more than one base class and one child class
"""class A:
    def add(self,x,y):
        print("addition",(x+y))

class B:
    def sub(self,m,n):
        print("subtract",(m-n))
class C:
    def mul(self,p,q):
        print("multiply",(p*q))
class Calculator (A,B,C):
    pass


c1=Calculator()
c1.add(5,7)
c1.sub(9,5)
c1.mul(7,8)"""



"""class A:
    __a=90
a1=A()
print(a1.__a)"""

