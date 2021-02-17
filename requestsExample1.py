#pip install requests
# service or API -- requests to API
#POST-- insert some info, GET--- ask for some info,PUT-- update some existing info,DELETE-- delete some existing info

import requests
import json
serverUrl=r"https://jsonplaceholder.typicode.com/posts"
response=requests.get(serverUrl)
print(response.content)
print(response.json())
str1=response.content
#datainPythonFormat=json.loads(response.json())#error loads --- str,byte, byte array
#JSON.stringify();
#JSON.parse() -- string back into json
datainPythonFormat=json.loads(str1)
print(datainPythonFormat)
print(type(datainPythonFormat))# list of dict True
print(type(response.json())) #json List true
print(type(response.content)) #bytes
print(type(response.text)) #str
#print(response.text)
str2=response.text
datainPythonFormat2=json.loads(str2)
print(datainPythonFormat2)

print(response.headers)# dictionary
print(response.headers["Content-Type"])

print(response.cookies) #cookie jar object

print("status",response.status_code)
print("status message",response.reason)

#flask
# post requests: insert some information
print("Response of post requests")
response=requests.post(serverUrl,data={"empId":999,"empName":"sara"})
print(response.status_code)
print(response.text)

print("Response of put requests")

#put -- modify the existing data
serverUrl=r"https://jsonplaceholder.typicode.com/posts/1"
response=requests.put(serverUrl,data={"id":1,"empId":999,"empName":"sara"})
print("status code",response.status_code)
print(response.text)

#delete
print("Response of delete requests")

serverUrl="https://jsonplaceholder.typicode.com/posts/1"
response=requests.delete(serverUrl)
print("status code",response.status_code)
print(response.text)
