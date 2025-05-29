import threading

def Small(str1):
    sum = 0
    for ch in str1:
        if ch.islower():
            sum += 1

    print("Total number of small case characters are :",sum)

def Capital(str1):
    sum = 0
    for ch in str1:
        if ch.isupper():
            sum += 1

    print("Total number of upper case characters are :",sum)

def Digits(str1):
    sum = 0
    for ch in str1:
        if ch.isdigit():
            sum += 1

    print("Total number of digits in string are :",sum)

def main():
    str1 = input("Enter string : ")

    small = threading.Thread(target=Small,args=(str1,))
    cap = threading.Thread(target=Capital,args=(str1,))
    dig = threading.Thread(target=Digits,args=(str1,))

    small.start()
    cap.start()
    dig.start()

    small.join()
    cap.join()
    dig.join()

    print("-----End of main------")


if(__name__ == "__main__"):
    main()