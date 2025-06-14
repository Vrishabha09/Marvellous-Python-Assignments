import os

def RemoveBlank(fName,destFile):
    Ans = os.path.exists(fName)
    if Ans:
        fd = open(fName,"r")
        fd2 = open(destFile,"w")
        for line in fd:
            if line.strip():
                fd2.write(line)
        
        print("New file",destFile,"created with no empty lines.")

    else:
        print("File not present in this directory.")
        

def main():
    fName = input("Enter file name : ")
    DFile = input("Enter new file name : ")
    RemoveBlank(fName,DFile)

if(__name__ == "__main__"):
    main()