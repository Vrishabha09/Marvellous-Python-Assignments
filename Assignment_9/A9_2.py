import multiprocessing
import os

def Display(iList):
    SquaredList = list()
    print("Displaying for Process :---------Process",os.getpid(),"--------")
    for data in iList:
        no = data**2
        SquaredList.append(no)
    print("Squared Element list :",SquaredList)

def main():
    no = int(input("Enter number of elements : "))

    iList = list()

    for i in range(no):
        data = int(input("Enter element : "))
        iList.append(data)

    print("Original list :",iList)
    P1 = multiprocessing.Process(target=Display,args=(iList,),name="P1")
    P2 = multiprocessing.Process(target=Display,args=(iList,),name="P2")
    
    P1.start()
    P1.join()

    P2.start()
    P2.join()

    print("----------End of main ----------")
if(__name__ == "__main__"):
    main()