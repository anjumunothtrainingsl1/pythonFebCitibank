#tuples and sets
#tuples -- enclosed with (); immutable; ordered
tuple1=(10,20,30,40,50)
tuple2=("iphone","samsung","nokia")
tuple3=(10,20,True,"hello")

print(tuple1)
print(tuple1[3])#40
print(tuple1[0:2])#(10,20)

for mobile in tuple2:
    print(mobile)
#updating an tuple -- no
#tuple1[0]=-99
#tuple1[2:4]=[100]
tuple4=(5,2,9,10)
print(tuple4);#(5,2,9,10)
tuple5=tuple1+tuple4
print(tuple5)#(10,20,30,40,50,5,2,9,10)
tuple1=tuple1+tuple4;# work(10,20,30,40,50,,5,2,9,10)
#extend,insert,append --no; remove; pop--no
print(len(tuple1))
tuple5=(tuple1,tuple2)
print(tuple5)

print(max(tuple1))
print(min(tuple1))
tuple6=tuple1+tuple2
print(tuple6)

#usecases of tuples --->
#1. colours of rainbow
#2. various cards
#3. read only constants

# avoid tuple1=tuple1+tuple2

list1=[10]
tuple7=(10,)
print(tuple7)
tuple8=(10,20,30)
x,y,z=tuple8
print(x,y,z)#x=10;y=20;z=30;sequence unpacking
#a,b=tuple8
#q,w,e,r=tuple8
#print(a,b)
#print(q,w,e,r)

# sequence packing -- into a tuple only
tuple9=1,2,3
print(tuple9);


j,k=[10,20]
print(j,k)

#sets
# collection of values; no duplicates; unordered collection
fruits={"apples","bananas","apples","strawberries"}
print(fruits)
print(len(fruits))
#union,intersection,difference,membership
fruits1={}# created a dictionary
fruits2=set()
print(fruits1)
print(fruits2)
set2=set("good morning")
print(set2)



