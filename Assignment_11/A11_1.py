def Display(no):
   if(no != 0):
       Display(no-1)
       print(no)         # Follows post-order behaviour
   else:
       return

def main():
    no = int(input("Enter number : "))
    Display(no)

if(__name__ == "__main__"):
    main()