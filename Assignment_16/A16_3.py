import os

#This functionality can be obtained using 4 ways
# 1. Using readlines and then for loop to count lines               Load full file(Slower)
# 2. Using readlines and then use len() method to count lines       Load full file(Slower)
# 3. Sum() methond which internally works like for loop but doesn't load full file sum(1 for line in file)
# 4. enumerate() method efficient as sum() but only used if you want index and line of file


def DisplayFile(fName):
    flag = os.path.exists(fName)
    Cnt = 0;

    if flag:
        fd = open(fName,"r")
        for line in fd:  # internally this is what sum method does
            Cnt += 1
        
        print("Number of lines in",fName,":",Cnt)
        fd.close()
    else:
       print("File not present in this directory.")
def main():
    fName = input("Enter file name : ")

    DisplayFile(fName)
if(__name__ == "__main__"):
    main()