class Square:
    ctr=0;#class var; shared across all the objects; one copy of it
    def __init__(self):
        self.side1=0 #instance var
        self.__privateVar=999
    def calcArea(self):
        print("Area =",self.side1*self.side1)
        Square.ctr+=1;
        print("Private var=",self.__privateVar)
        print("Ctr",Square.ctr)
        self.area=self.side1*self.side1
    def calAreaWithValue(self,p1):
        self.side1+=p1;
        self.calcArea()

sqObj=Square();
sqObj.side1=10;
sqObj.calcArea();#ctr=1
sqObj.calAreaWithValue(5)#ctr=2
sqObj2=Square();
sqObj2.side1=30;
sqObj2.calcArea(); #ctr=3
print(Square.ctr)
#print("Private var outside the class",sqObj2.__privateVar)
print("Area =",sqObj2.area)
#OOPs-- abstraction(data hiding,public ,private),encapsulation(classes ,objects; one logical unit),
# inheritance(simple,multiple,multilevel,hybrid),polymorphism
#simple inheritance Father son
#multi level inheritance --> Granddad, dad, Child
#multiple --> (father,mother)-->child; Java (no)
#hybdid --> rhombus-- A-->(B,C)-->D

class Shape:
    def __init__(self,p1,p2):
        self.side1=p1
        self.side2=p2
    def display(self):
        print(self.side1)
        print(self.side2)

class Cuboid(Shape):
    def __init__(self,p1,p2,p3):
        Shape.__init__(self,p1,p2)
        self.side3=p3
    def displayDetails(self):
        self.display()
        print(self.side3)

cuboibObj=Cuboid(1,2,3)
cuboibObj.displayDetails()

class Colour:
    def __init__(self,p1):
        self.colour=p1
    def display(self):
        print(self.colour)

#multiple inheritance
class Cube(Shape,Colour):
    def __init__(self,p1,p2,p3):
        Shape.__init__(self,p1,p2)
        Colour.__init__(self,p3)
    def printDetails(self):
        #self.display()
        Shape.display(self)
        #print("Colour",self.colour)
        Colour.display(self)

cubeObj=Cube(10,20,"pink")
cubeObj.printDetails()
#shape's display using cube's obj
print("*"*40)
cubeObj.display()
Shape.display(cubeObj)
#colour's display using cube's obj
Colour.display(cubeObj)


#upcasting downcasting
#java
#Class base, Class Derived extends Base
#Derived dobj=new Base()

#polymorphism ;function overloading-- no; function overwriting;fuction overriding
class Example:
    def __init__(self,p1):
        self.side1=p1
    def __init__(self):
        self.side1=0

obj1=Example();
print("Obj1",obj1.side1)
obj2=Example()
print("Obj2",obj2.side1)

#function overriding-- inheritance; same function name; same parameters
class Shape1:
    def __init__(self,p1,p2):
        self.side1=p1
        self.side2=p2
    def display(self):
        print(self.side1)
        print(self.side2)

class Cuboid1(Shape1):
    def __init__(self,p1,p2,p3):
        Shape1.__init__(self,p1,p2)
        self.side3=p3
    def display(self):
        print("Cuboid1 display")
        print(self.side1)
        print(self.side2)
        print(self.side3)
    #override an inbilt method
    def __str__(self):
        str1="Side 1:"+str(self.side1)+" Side 2:"+str(self.side2)+" Side 3:"+str(self.side3)
        return str1
    def __add__(self, other):
        return Cuboid1(self.side1+other.side1,self.side2+other.side2,self.side3+other.side3)
cuboidObj1=Cuboid1(10,20,30)
cuboidObj1.display()
print(cuboidObj1)
cuboidObj2=Cuboid1(5,5,5)
cuboidObj3=cuboidObj2+cuboidObj1;
print(cuboidObj3)

# constructor overloading -- not possible
#Cuboid1(1)
#Cuboid1(1,2,3)
#Cuboid1([10,20,30])

class Cuboid2:
    def __init__(self,p1,p2,p3):
        self.side1=p1
        self.side2 = p2
        self.side3 = p3

    def __str__(self):
        str1 = "Side 1:" + str(self.side1) + " Side 2:" + str(self.side2) + " Side 3:" + str(self.side3)
        return str1

    @classmethod
    def fromList(cls,list1):
        #cls is a refernce to the class
        obj=cls(list1[0],list1[1],list1[2])
        return obj

cObj=Cuboid2(10,20,30)
print(cObj)
cObj2=Cuboid2.fromList([22,33,44])
print(cObj2);



#static method
# utility functions

class MyList:
    @staticmethod
    def slice(list1, pos, delCount, *insertElements):
        del list1[pos:(pos + delCount)]
        print(insertElements);  # (77,88)
        ctr = 0
        for item in insertElements:
             list1.insert(pos + ctr, item)
             ctr += 1


marks=[10,20,30,40,50,60]
MyList.slice(marks,2,2,99,88,77)
print(marks)#[10,20,99,88,77,50,60]


#classMethod decorator -- return a new object; overloading of constructor
#static method decorator- create a static function which can be called without an object
# utility functions

"hello".lower()

class Employee:
    def __init__(self,p1,p2):
        self.empId=p1
        self.__salary=p2
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if(value<=0):
            pass
        else:
            self.__salary=value
    def __str__(self):
        return "EmpId"+str(self.empId)+"salary"+str(self.salary)

sara =Employee(101,898)
sara.salary=123
print(sara)
sara.salary=-123
print(sara)

#Working with Files; Design Patterns; request module Rest Api
#@property,@classmethod, @staticdecorator, custom decoratos