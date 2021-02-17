#deserializing Json
#python    #json
import json
try:
    with open(r"C:\Users\anjum\OneDrive\Desktop\citibank-python\zipcode.json","r") as filePtr:
        dataInPythonFormat=json.load(filePtr)
        print(dataInPythonFormat)
        for i in range(10):
            print(dataInPythonFormat[i])
except Exception as e:
    print(e)


str1='''
{"empId":101,"empName":"sara","salary":989,"score":[3.5,4.5],"status":false}
'''
dataInPythonFormat2=json.loads(str1)
print(dataInPythonFormat2)


#a+b

with open("config.json","r") as filePtr:
    data=json.load(filePtr)
    sum1=data["a"]+data["b"]
    print(sum1)

with open("input2.txt","r") as filePtr:
    data=filePtr.read();
    mydata=data.split(";")
    print(mydata)
    myA=mydata[0].split("=")[1]
    myB = mydata[1].split("=")[1]
    sum1=myA+myB; #"10"+"20" 1020
    print(sum1)



