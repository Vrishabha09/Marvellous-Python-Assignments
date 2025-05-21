
Area = lambda l, b : l*b

Perimeter = lambda l, b: 2*(l+b)
def main():
    length = float(input("Enter length : "))
    width = float(input("Enter width : "))

    ans = Area(length,width)
    print("Area :",ans)

    ans = Perimeter(length,width)
    print("Perimeter :",ans)
if(__name__ == "__main__"):
    main()