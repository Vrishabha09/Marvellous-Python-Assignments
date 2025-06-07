
class Employee:
    emp_id = 100
    def __init__(self,n,s):
        self.Name = n
        self.Sal = s

    @classmethod
    def EmployeeId(cls):
        cls.emp_id += 1

    def Display(self):
        print("Employee Id :",Employee.emp_id,"Name :",self.Name,"Salary :",self.Sal)

def main():
    emp1 = Employee("Vrishabh Pawar",300000)
    emp1.EmployeeId()
    emp1.Display()

    emp2 = Employee("Sarthak Pawar",400000)
    emp2.EmployeeId()
    emp2.Display()

    emp3 = Employee("Shubham Pawar",500000)
    emp3.EmployeeId()
    emp3.Display()
if(__name__ == "__main__"):
    main()