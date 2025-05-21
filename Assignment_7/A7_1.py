Square = lambda no : no**2

Cube = lambda no : no**3

def main():
    no = int(input("Enter one number : "))

    ans = Square(no)
    print("Square :",ans)

    ans = Cube(no)
    print("Cube :",ans)
    
if(__name__ == "__main__"):
    main()