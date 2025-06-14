import os

def DisplayWord(fName):
    flag = os.path.exists(fName)

    if flag:
        fd = open(fName,"r")
        for line in fd:
            words = line.split()
            for word in words:
                if len(word) >= 5:
                    print(word)
        
        fd.close()
    else:
       print("File not present in this directory.")
def main():
    fName = input("Enter file name : ")

    DisplayWord(fName)
if(__name__ == "__main__"):
    main()