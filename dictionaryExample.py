#dictionary
#key value parirs ; enclosed with {}
#keys: Immutable types: string,number,tuple
#values: any dt

emp={"empId":101,"empName":"sraa","salary":9898}
print(emp)
print(emp["empId"])

del emp["salary"]
print(emp)

emp["deptId"]="d1"
print(emp)
print(list(emp))

for key,value in emp.items():
    print(key ," : ",value)

#emp.keys()
#emp.values()

print(emp.keys())
print(emp.values())

for key in emp.keys():
    print(key,":",emp[key])

for value in emp.values():
    print(value)

emp1={"empId":102,"empname":"tara","temp":102}
print(emp1)
for value in emp1.values():
    print(value)

qusetions=("name","emailId","phoneNumber")
answers=("anju","anjumunoth@gmail.com",7899)
for q,a in zip(qusetions,answers):
    print("What is your {0}. It is {1}".format(q,a))


#list of dict
empList=[]
empList.append({"empId":101,"empName":"sraa","salary":9898})
empList.append({"empId":102,"empName":"tara","salary":9898})
empList.append({"empId":103,"empName":"lara","salary":9898})
empList.append({"empId":104,"empName":"geeta","salary":9898})
print(empList)

for employee in empList:
    print(employee["empName"],end="  ")
print()
print(empList[3])

empList[3].get("empId") #104
empList[3]["empId"]

emp3={"empId":101,"empName":"sraa","salary":9898}
print(emp3)
emp3.clear()
print(emp3)

emp3={"empId":101,"empName":"sraa","salary":9898}
emp4=emp3.copy()
emp4["empId"]=999
print("Emp3 ",emp3)
print("Emp4 ",emp4)
#shallow copy; deep copy
#copy --- shallow copy
emp5={"empId":101,"empName":"sraa","salary":9898,"address":{"street":879,"pincode":8798}}
emp6=emp5.copy()
emp5["address"]["street"]=1
emp5["empName"]="jack"
print("Emp5 ",emp5)
print("Emp6 ",emp6)





