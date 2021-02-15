#list datatype
list1=[10,20,30,40,50]
fruits=["apple","pineapples","strawberries"]
list2=[10,23.45,True,"hello","citbank","training"]

print(list1)
print("First fruit"+fruits[0])
print("Range of values",list2[2:5])
print("&".join(fruits))
#generic array or array -- not there in python

for i in range(len(list1)):
    print(i,list1[i])

for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i,end=" ")#
for i in range(1, 16):
    print(i)
print("*"*40)
for i in range(2,17,2):
    print(i)

for i in range(2,17,2):
    print(i,end=" ")


str1="happy"
str2=str1*3;#happyhappyhappy
print(str2)
str1="1"
str2=str1*5;
print(str2);#11111

# update the list
for i in range(0,len(list1),2):
    print(list1[i],end =" ");#[10,30,50]

list1=[10,20,30,40,50,60]
print();
list1[0]=1000;
#list1[10]=900#wrong ; out of range;
list1[-2]=800# correct[1000,20,30,40,800,60]
print(list1);
#[1000,20,30,40,800,60];

list1=[10,20,30,40,50,60]
#list1[6]=1000 #exception out of range
#list1[2:5]=1000# exception;
list1[2:5]=[1000];print(list1)#;[10,20,1000,60]
list1=[10,20,30,40,50,60];list1[2:5]=[1000,2000,3000]#[10,20,1000,2000,3000,60]
list1=[10,20,30,40,50,60];
list1[2:5]=[1000,1,2,3,4,5,6,7]#[10,20,1000,1,2,3,4,5,6,7,60]
print(list1)
list1[2:6]=[1000]
#list1[6]=70;
#
# append an item(s)
list1=[10,20,30,40,50,60];
list1.append(70)
print(list1);

list1.extend([80,90,100])
print(list1);#[10,20,30,40,50,60,70,80,90,100];

list1.insert(3,5);#[10,20,30,5,40,50,60,70,80,90,100];
print(list1)

list1.insert(3,[1,2]);#[10,20,30,[1,2],5,40,50,60,70,80,90,100]
print(list1)

subArray=list1[3]
print(subArray[0])#1

list1[3][0]=-99
#remove elements
print(list1.pop())
print(list1.pop(1))
#pop(index=-1)
print(list1)

print(list1.pop(2))
list1.remove(60)
print(list1)

list1=[10,20,30,10,40]
print("Output of remove",list1.remove(10));#[20,30,10,40]
#print(list1.remove(60));# error
print(list1)

list1=[10,20,30,10,40]
valueToBeRemoved=input("Enter the value to be removed")
print("Count of occurences",list1.count(int(valueToBeRemoved)))
ctr=list1.count(int(valueToBeRemoved))

while(ctr>=1):
    print("Inside the loop")
    ctr-=1
    list1.remove(int(valueToBeRemoved))
print("List after removal",list1)







