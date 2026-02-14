#oops concepts in python corey

# lec 1 

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

class Employee2:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1  = Employee2("Corey", "Schafer", 50000)
emp2  = Employee2("Test", "User", 60000)

print("Employee 2 email: ",emp1.email)
print("Employee 2 email: ",emp2.email)

print("Employee 2 fullname: ",emp1.fullname())
print("Employee 2 fullname: ",emp2.fullname())

print("Employee 2 fullname: ",Employee2.fullname(emp1))
print("Employee 2 fullname: ",Employee2.fullname(emp2))

# lec 2 