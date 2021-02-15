print("Welcome to the training on python")

# declaration cannot be done;is not needed
#data types : number(int, float,complex); string; boolean
#dynamic data type; type inference
i=10
i="hello"
i=True
i='hello'
i='''This is a string
spanning across multiple lines
'''
i=""" Yesterday was Valentine's day
"""
i="Yesterday was Valentine's day"
i='"Yesterday" was Valentine"s day'
i='Yesterday was Valentine\'s day'
i="'Yesterday'"+'"to the training"'
print(i);print("Thank you")
i=10;j=20;k=True
print("The value of i"+ str(i)+str(j)+str(k))
print("The value of i is :",i,j,k);
# print() ---> one arg --- string
#print("hello"+"citibank")
#print("hello",i)
print("hello",i,end="$")# id end is not provided the default valus of new line will be taken
print("this will also be printed on the same line as i")
print("Bye")

i=j=k=10
print(i,j,k)

a,b,c=10,20,30
print(a,b,c)
#print(d) NameError

#d,e,f=20,30 #ValueError
#print(d,e,f)

i=10.76878
j=float(4.76879)
#Good Morning
#012345
str1="Good morning"
print(str1.lower())
str1.upper()
str1.capitalize()
str1.lower()
print(str1)
# string immutable
str2="c:/users/desktop/new"
print(str2)
str2=r"c:\users\desktop\new\readme.txt"
print(str2)
print(str1.startswith("morning",5,7))
#print(str1.startswith("morning"))
#print(str1.startswith("morning",end=7,beg=5))

print(str1.endswith("Good",0,4))

#isdigit; istitle; islower; isupper; isalpha;isalnum; isspace

#index find
#find -- index or -1
str1="Good Morning"
print(str1.find("or"))
print(str1.find("or",0,4))# -1
print(str1.find("z"))

#index -- str, start,end; return index or exception
print(str1.index("or"))#6
#print(str1.index("or",0,4))# raise an exception ValueError
#print(str1.index("z")) #raise an exception

print("length of the string:" ,len(str1))
#join(sequence)
sequence=("hello citibank","team")
seperator="_"

print(seperator.join(sequence))

#split
str1="Today is a beautiful day"
print(str1.split())

arr=str1.split()
str2=" ".join(arr)
print(str2)

str1="Today is a beautiful day"
arr=str1.split("a"); # return me an array ["Tod","y is "," be","utiful d","y"];
str2="a".join(arr);
print("Str2: "+str2)
# "Today is a beautiful day"

#substring, substr,slice -- no methods in python; slice operator
str1[0:3]












