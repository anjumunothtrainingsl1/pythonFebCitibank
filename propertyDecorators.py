def star(func):
    def innerFunc(*args,**keywordargs):
        print("*"*40)
        func(*args,**keywordargs);#func(("anju"),{lastName:"munoth"})
        print("*"*40)
    return innerFunc;

def percent(f1):
    def innerFunc(*args,**kwargs):
        print("%"*40)
        f1(*args,**kwargs);
        print("%"*40)
    return innerFunc;

@star
@percent
def myFunc(p1,lastName):
    print("hello from",p1 )
    print("Thank for logging ur information",lastName)
myFunc("anju","munoth")

#propertyDecorator
#myFunc=star(myFunc);#print("*");func();print("*")
#myFunc=percent(myFunc)#print(%)print("*")func();print(*)print(%)
#myFunc("anju","munoth")