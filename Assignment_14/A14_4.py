
class School:
    School_Name = " "

    def __init__(self,n,r):
        self.Name = n
        self.RollNo = r

    def Display(self):
        print("School Name :",School.School_Name)
        print("Student Name :",self.Name,"| Roll no :",self.RollNo)

def main():
    sobj = School("Vrishabha Pawar",33)
    School.School_Name = "J N Petit Technical High School"
    sobj.Display()

    sobj1 = School("Shubham Pawar",16)
    School.School_Name = "J S Tyagi"
    sobj1.Display()
if(__name__ == "__main__"):
    main()