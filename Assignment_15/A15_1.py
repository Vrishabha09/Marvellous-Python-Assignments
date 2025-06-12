import os

def ChkFile(fName):
    Ans = os.path.exists(fName)
    return Ans

def main():
    fName = input("Enter file name : ")
    ret = ChkFile(fName)

    if ret:
        print("File is present")
    else:
        print("File not present")

if(__name__ == "__main__"):
    main()