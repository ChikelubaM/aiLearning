# 1. Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name

# SOLUTION
class Employee:
    def __init__(self, i, n):
        self.id = i
        self.name = n

    def display(self):
        print (f"ID: {self.id}, \nName: {self.name}")

# object initializes id and name dynamically for every Employee object created.
emp = Employee(1, "coder")

emp.display()
# 2. Use del property to first delete id attribute and then the entire object

del emp.id
try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined")

del emp
try:
    emp.display()
except NameError:
        print("name is not defined")