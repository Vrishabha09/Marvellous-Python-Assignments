powr = 1

def Power(x,n):
    global powr
    if n > 0:
        powr *= x
        Power(x,n-1)
    
    return powr

def main():
    x = int(input("Enter number : "))
    n = int(input("Enter power to be calculated : "))

    ret = Power(x,n)

    print("Answer :",ret)
if(__name__ == "__main__"):
    main()