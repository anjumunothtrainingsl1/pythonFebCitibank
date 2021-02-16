def myFunc1(p1,p2):
    "function docstring"
    temp=p1;p1=p2;p2=temp;

a,b=10,20
myFunc1(a,b)
print("a=",a,"b=",b)

def myFunc2(list1):
    list1[2]=1000

myList=[10,20,300,40,50]
myFunc2(myList)
print(myList);#pass by ref

def myFunc3(p1,p2):
    return(abs(p1)+abs(p2))

result=myFunc3(-5,-10)#positional args
print(result)

result=myFunc3(p2=-5,p1=-10)#keyword args
print(result)

result=myFunc3(-5,p2=-10)#positional args,keyword args
print(result)

def myFunc4(str1,start,end):
    print(str1[start:end])

#myFunc4(str1="hello",0,2)
myFunc4(str1="hello",start=0,end=2)
#myFunc4(str1="hello",0,end=2)
#myFunc4("hello",start=0,2)
myFunc4("hello",0,end=2)

def myFunc5(list1,pos,delCount,*insertElements):
    del list1[pos:(pos+delCount)]
    print(insertElements);#(77,88)
    ctr=0
    for item in insertElements:
        list1.insert(pos+ctr,item)
        ctr+=1

myList=[10,20,30,40,50]
myFunc5(myList,2,1,77,88);#[10,20,77,88,40,50]
print(myList)


myFunc5(myList,2,1,77,88)
myFunc5(myList,2,1)
myFunc5(myList,2,1,77,88,99,11,22)
myFunc5(myList,2,1,77)
myFunc5(myList,2,1,77,"hello","citibank","python",[33,44],{1,2,3,1,2,3},("a","b"))
print(myList)

# default args
def myFunc6(p1,p2=12):
    print(p1+p2)
myFunc6(100)
myFunc6(100,200)
myFunc6(p2=20,p1=100)
myFunc6(100,p2=29)
myFunc6(p1=99)
#positional args --- args -- tuple
#keyword args -- keywordArgs --- dict
def myFunc7(*args,**keywordArgs):
    print("Positional args",args)
    print("keyword args:",keywordArgs)
    print("*"*40)

myFunc7(10,20,30)#only positional args
myFunc7(empId=101,empName="sara",salary=6878)
myFunc7(10,20,30,empId=101,empName="sara",salary=6878)

#anonymous function lambda
#can take any number of args;
#return an expression only; cant have any commands
#local namespace; can access the global var and the local var
#similar to inline fuctions

sum1=lambda p1,p2:p1+p2;
print(sum1(10,20))

globalTotal=0

def myFunc7():
    return("Normal function:thank u team" +str(globalTotal))
print(myFunc7())
def myFunc8():
    localVar=100
    message=lambda  :"Lambda function:thank u team"+str(localVar)
    print(message())
myFunc8()


#closure functions
def myFunc8():
    ctr=0
    def innerFunc():
        return ctr
    return innerFunc

resultFunc=myFunc8()#scope of ctr is over
result=resultFunc()# access to ctr is possible
print("Finl result",result); #0

def myFunc9(n):
    def multiplier(x):
        return x*n;
    return multiplier;
Table3=myFunc9(3)
Table5=myFunc9(5);

print(Table3(9))
print(Table5(9))

def pretty(f1):
    def innerFunc():
        print("*"*40);
        f1();
        print("*"*40);
    return innerFunc;

def printHello():
    print("hello")

printHello=pretty(printHello)
printHello()
x=pretty(printHello)
x()


def divideTwoNumbers(a,b):
    return a//b

def divideTwoNumbersClosurefunc(f1):
    def innerFunc(*args,**kwargs):
        if(args[1]==0):
            newargs=();
            for i in range(len(args)):
                if(i==1):
                    newargs[1]=1
                else:
                    newargs[i]=args[i]
        return f1(*newargs,**kwargs)

    return innerFunc;
divideTwoNumbers=divideTwoNumbersClosurefunc(divideTwoNumbers)
print("Result",divideTwoNumbers(10,0))
print("Result",divideTwoNumbers(10,2))