def DisplayCount(name):
    length = len(name)
    print(length);

def main():
    name = input("Enter name to count its length: ");
    DisplayCount(name);

if(__name__ == "__main__"):
    main()