import os

def ChkFreq(fName,string):
    Ans = os.path.exists(fName)
    Cnt = 0;
    if Ans:
        fd = open(fName,"r")

        for line in fd:
            words = line.split()
            for word in words:
                if word == string:
                    Cnt += 1

        fd.close()
        print("Frequency of",string,":",Cnt)
    else:
        print("File not present.")


def main():
    fName = input("Enter file name : ")
    string = input("Enter String to check frequency : ")

    ChkFreq(fName,string)

if(__name__ == "__main__"):
    main()