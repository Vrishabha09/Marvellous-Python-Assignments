def DisplayPattern(no):

    for i in range(no):
        for j in range(no):
            if(i > j):
                print("*",end=" ")
            elif(i == j):
                print("*",end=" ")
        print("")

def main():
    DisplayPattern(4)
if(__name__ == "__main__"):
    main()