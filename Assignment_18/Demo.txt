import os

def ChkFile(fName):
    flag = os.path.isfile(fName)

    return flag

def main():
    fName = input("Enter file name : ")
    Ret = ChkFile(fName)

    if Ret:
        print("File is present.")
    else:
        print("File is not present.")
if(__name__ == "__main__"):
    main()