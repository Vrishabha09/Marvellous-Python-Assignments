import os

def WriteFile(students,fName):

    flag = os.path.exists(fName)

    if flag:
        Border = "-"*80
        print(Border)
        print("File "+fName+" already present in this directory.")
        print("If you still want to proceed.\nChoose any one option.")
        print("1.a(Append to existing data).\n2.w(Will overwrite the file.)")
        print(Border)
        Choice = str(input("Enter your choice : "))

        if Choice == "a":
            fobj = open(fName,"a")

            for student in students:
                student = str(student)
                fobj.write(student+"\n")
            fobj.close()
            print("Data appended in",fName)

        elif Choice == "w":
            fobj = open(fName,"w")

            for student in students:
                student = str(student)
                fobj.write(student+"\n")
            fobj.close()
            print("Data over written in",fName)
        else:
            print("Enter proper choice.\nEither 'a' or 'e'.")
    else:
        fobj = open(fName, "x")

        for student in students:
            student = str(student)
            fobj.write(student+"\n")
        fobj.close()
        print("New file created",fName,"and student data succesfully written")

def main():
    students = list()
    fName = input("Enter file name : ")

    iNo = 10
    print("Enter 10 numbers")

    for i in range(iNo):
        no = int(input(f"Numbers[{i+1}] "))
        students.append(no)

    WriteFile(students,fName)
if(__name__ == "__main__"):
    main()