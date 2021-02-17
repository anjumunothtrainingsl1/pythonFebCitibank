import csv
with open("emp2.csv") as filePtr:
    reader=csv.reader(filePtr,delimiter=",")
    ctr=0;
    print(reader)#list of list
    for row in reader:
        if(ctr==0):
            headerInfo=row
            ctr+=1
        else:
            print(headerInfo[0],":",row[0])
            print(headerInfo[1], ":", row[1])
            print(headerInfo[2], ":", row[2])
            print(row)
            print("*"*40)


with open("emp2.csv") as filePtr:
    reader=csv.DictReader(filePtr)
    ctr=0
    for row in reader:
        if ctr==0:
            print(row)
            ctr+=1
        else:
            print(row["emp_id"])
            print(row["emp_name"])
            print(row["sal"])