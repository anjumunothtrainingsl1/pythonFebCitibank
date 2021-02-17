import csv

with open("emp.csv","w") as filePtr:
    emp_writer=csv.writer(filePtr,delimiter=",",quoting=csv.QUOTE_NONNUMERIC,lineterminator="\n")
    emp_writer.writerow([101,"sara",1234])
    emp_writer.writerow([102, "tara", 1234])
    emp_writer.writerow([103, "lara", 1234])
    emp_writer.writerows([(104,"geeta",8798)])

listarr=[{"emp_id":101,"emp_name":"sara","sal":90},{"emp_id":102,"emp_name":"tara","sal":190},{"emp_id":103,"emp_name":"lara","sal":920}]

with open("emp2.csv","w") as filePtr:
    fieldNames=["emp_id","emp_name","sal"]
    emp_writer=csv.DictWriter(filePtr,delimiter=",",quoting=csv.QUOTE_NONNUMERIC,fieldnames=fieldNames,lineterminator="\n")
    emp_writer.writeheader()
    for i in range(len(listarr)):
        emp_writer.writerow(listarr[i])
