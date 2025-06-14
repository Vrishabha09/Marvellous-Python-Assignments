import os

def DisplayFile(fName):
    Ans = os.path.exists(fName)
    if Ans:
        fd = open(fName,"r")
        for line in fd:
            words = line.split()
            if (int(words[2]) >= 75):
                print(line)
    else:
        print("File not present in this directory.")
        

def main():
    fName = input("Enter file name : ")
    DisplayFile(fName)

if(__name__ == "__main__"):
    main()