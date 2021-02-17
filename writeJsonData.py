#serialising
# converting the data which is in python data types to json data type
import json
emp={"empId":101,"empName":"sara","salary":87989.879,"status":True,"projects":("p1","p2")}
listarr=[{"emp_id":101,"emp_name":"sara","sal":90},{"emp_id":102,"emp_name":"tara","sal":190},{"emp_id":103,"emp_name":"lara","sal":920}]

with open("emp.json","w") as filePtr:
    json.dump(emp,filePtr);

empDataInJson=json.dumps(emp)
print("data in json format",empDataInJson)
