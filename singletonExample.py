def mySingleton(cls):
    def innerFunc(*args, **kwargs):
        if not innerFunc.instance:
            innerFunc.instance = cls(*args, **kwargs)
        return innerFunc.instance
    innerFunc.instance = None
    return innerFunc

@mySingleton
class Emp:
    def __init__(self,p1,p2):
        self.empId=p1
        self.empName=p2
    def __str__(self):
        return "Employee details : "+str(self.empId)+self.empName

sara=Emp(101,"sara")
lara=Emp(102,"lara")
print(sara)
print(lara)
print(id(sara))
print(id(lara))

@mySingleton
class Shape:
    def __init__(self):
        self.side1=100

shapeObj=Shape()
shapeObj2=Shape()
print(shapeObj.side1)
print(shapeObj2.side1)
shapeObj2.side1=99
print(shapeObj.side1)
print(shapeObj2.side1)


