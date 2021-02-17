try:
    with open("input2.txt","w",encoding="utf-8") as filePtr:
        filePtr.write("Welcome to RPS")
        filePtr.write("Hope the training is clear")
        filePtr.writelines(["This is line1","This is line2"])
except Exception as e:
    print(e)

#file doesnot exist : read-- exception; write: create the file; append: create the file
#file large -- text;
