#files :open,manipulate(read,write,append),close
#mode : r, w, a, t, b(binary used for non text files like images or exe), x, r+b, w

try:
    fileUrl=r"C:\Users\anjum\OneDrive\Desktop\file1.txt"
    filePtr=open(fileUrl,"r",encoding="utf-8")
    #perform file operations
    print(filePtr.read(5))#read the first 5 data
    filePtr.seek(0);#0 - from the beg of the file
    print(filePtr.read())
    filePtr.seek(0);  # 0 - from the beg of the file
    for line in filePtr:
        print(line,end=" ")
    print()
    filePtr.seek(0);  # 0 - from the beg of the file
    print(filePtr.readline())

except ZeroDivisionError:
    print("Zero Division Error")
except Exception as e:
    print("Error working with the file")
    print(e)
finally:
    if(filePtr):
        filePtr.close()

