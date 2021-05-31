class employee:
    no_of_leaves=8

    def __init__(self, aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary}. and role is {self.role} "
    @classmethod
    def change_of_leaves(cls,anumber):
        cls.no_of_leaves=anumber
    
E1=employee("Shreyas","25000","doctor")
E1.name="back"
E1.salary="50000"
print(E1.salary)
E3=employee('car','pen','sock')
# E3.change_of_leaves(67)
# print(E3.no_of_leaves)
# print(E1.salary)
e2=E1.printdetails()
print(e2)