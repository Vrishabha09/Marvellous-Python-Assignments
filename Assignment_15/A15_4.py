import os
import sys
import filecmp


# For a quick check if files are identical based on metadata, use filecmp.cmp(shallow=True).                
# For a precise content comparison, use filecmp.cmp(shallow=False).                                         #Slower but accurate
# For detailed, line-by-line differences, use difflib.                                                      #Provides detailed line by line comparison (Can be useful while comparing 2 files having minor differences, to trace those differences)
# For simple content comparison of small files, use the == operator.


def CmpFile2(fName1,fName2):
    flag1 = os.path.exists(fName1)
    flag2 = os.path.exists(fName2)

    if flag1 and flag2:
        if filecmp.cmp(fName1,fName2,shallow=False):
            print("Files are identical")
        else:
            print("Files do not have same content.")

def CmpFile(fName1,fName2):
    flag1 = os.path.exists(fName1)
    flag2 = os.path.exists(fName2)

    if flag1 and flag2:
        fd1 = open(fName1,"r")
        fd2 = open(fName2,"r")

        f1Content = fd1.read()
        f2Content = fd2.read()

        if f1Content == f2Content:
            print("Contents of both files is same.")
        else:
            print("Files contain different contents.")

        fd1.close()
        fd2.close()
    else:
        print("File not present") 

def main():
    
    if len(sys.argv) == 3:
        fName1 = sys.argv[1]
        fName2 = sys.argv[2]

        CmpFile(fName1,fName2)

    elif len(sys.argv) == 2:
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the file in below way.")
            print("File_name.py File1_name File2_name")
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This file is used to compare contents of 2 files are same or not.")

    else:
        print("Enter proper choice.")
        print("--u for usage of file(File_name.py --u).\n--h for help(File_name.py --h).")

if(__name__ == "__main__"):
    main()