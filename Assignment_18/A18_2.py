import os

def DisplayFile(fName):
    flag = os.path.isfile(fName)
    if flag:
        fd = open(fName,"r")

        for line in fd:
            print(line)
    else:
        print("File not present.")

def main():
    fName = input("Enter file name : ")
    DisplayFile(fName)

if(__name__ == "__main__"):
    main()