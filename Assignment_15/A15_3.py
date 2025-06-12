import os
import shutil

def CopyFile2(fName,srcFile):
    # Use shutil.copy2() if you need to preserve all metadata.                                  #Over writes data
    # Use shutil.copy() if you only need to preserve the file's permission mode.                #Over writes data
    # Use shutil.copyfile() if you only need to copy the content and don't need any metadata.   
    # Use shutil.copyfileobj() for more control over the copying process.

    shutil.copy2(srcFile,fName)



def CopyFile(fName,srcFile):
    Ans = os.path.exists(fName)
    if Ans:
        Border = "-"*80
        print(Border)
        print("File "+fName+" already present in this directory.")
        print("If you still want to proceed.\nChoose any one option.")
        print("1.a(Append to existing data).\n2.w(Will overwrite the file.)")
        print(Border)
        Choice = str(input("Enter your choice : "))

        if Choice == "a":
            fobj = open(fName,"a")
            fobj2 = open(srcFile,"r")

            data = fobj2.read()

            fobj.write(data)

            fobj.close()
            fobj2.close()

        elif Choice == "w":
            fobj = open(fName,"w")

            fobj2 = open(srcFile,"r")

            data = fobj2.read()

            fobj.write(data)

            fobj.close()
            fobj2.close()
        else:
            print("Enter proper choice.")
    else:
        fobj = open(fName, "x")
        fobj2 = open(srcFile,"r")

        data = fobj2.read()

        fobj.write(data)

        fobj.close()
        fobj2.close()

def main():
    fName = input("Enter file name you want to create : ")
    srcFile = "A15_2.py"
    CopyFile(fName,srcFile)

if(__name__ == "__main__"):
    main()