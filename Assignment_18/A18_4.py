import os
import filecmp
import sys

def CmpFile(fName1,fName2):
    flag1 = os.path.isfile(fName1)
    flag2 = os.path.isfile(fName2)
    if flag1 and flag2:
       Ret = filecmp.cmp(fName1,fName2,shallow=False)

       if Ret:
           print("Success.")
       else:
           print("Failure.")
           
    else:
        print("File not present.")

def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this file.")
            print("File_Name.py File1_name File2_name")
        elif sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This file compares two files.")
    elif len(sys.argv) == 3:
        fName1 = sys.argv[1]
        fName2 = sys.argv[2]
        CmpFile(fName1,fName2)
    else:
        print("Invalid arguements.")
        print("Enter any of 2 commands.\n1. FileName.py --u(Usage).\n2. FileName.py --h(Help)")

if(__name__ == "__main__"):
    main()