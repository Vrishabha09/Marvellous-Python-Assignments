import os

def DisplayFile(fName):
    flag = os.path.exists(fName)

    if flag:
        fd = open(fName,"r")
        data = fd.read()
        print("---------Data from file---------")
        print(data)
        print("--------------------------------")
        fd.close()
    else:
       print("File not present in this directory.")
def main():
    fName = input("Enter file name : ")

    DisplayFile(fName)
if(__name__ == "__main__"):
    main()