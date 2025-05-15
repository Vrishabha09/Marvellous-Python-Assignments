def isPrime(no):
    if no <= 1:
        return False
    for i in range(2, int(no/2) + 1):
        if no % i == 0:
            return False
    return True

def main():
    no = int(input("Enter number: "))
    if isPrime(no):
        print(no, "is a prime number.")
    else:
        print(no, "is not a prime number.")

if __name__ == "__main__":
    main()
