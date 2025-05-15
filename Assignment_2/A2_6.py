# pattern input : 5
#   *  *  *  *  *       (1,1) (1,2) (1,3) (1,4) (1,5) 
#   *  *  *  *          (2,1) (2,2) (2,3) (2,4)
#   *  *  *             (3,1) (3,2) (3,3)
#   *  *                (4,1) (4,2)
#   *                   (5,1)

def DisplayPattern(no):
    for i in range(no,0,-1):
        for j in range(i):
            print("*",end="  ")
        print(" ")

def main():
    no = int(input("Enter number: "))
    DisplayPattern(no);

if(__name__ == "__main__"):
    main()