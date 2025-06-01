def DisplayPattern(i, j):
    if i == 0:
        return
    if j < i:
        DisplayPattern(i, j + 1)
        print("*", end=" ")
    else:
        DisplayPattern(i - 1, 0)
        print()  

def main():
    no = int(input("Enter number : "))
    DisplayPattern(no, 0)

if __name__ == "__main__":
    main()
