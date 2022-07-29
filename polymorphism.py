# inherit, extend (the functionality of base class), override


# Employee is the base/parent class
class Employee:
    def __init__(self, name, age, salary):
        # constructor
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working...")

# a child class inherits all the attributes and functions/methods of base/parent class
# in this case, SoftwareEngineer and Designer are sub/child classes
# both child classes inherits Employee
class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)     # to call the initializer of the parent class (don't need to re-init)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging...")

    # overriding the work function from Employee class
    def work(self):
        print(f"{self.name} is coding...")

class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing...")

    # overriding the work function from Employee class
    def work(self):
        print(f"{self.name} is designing...")


# Polymorphism
#   -> related to inheritance
#   -> means many shape
#   -> we can make code that works on super class but it also work on any sub-class
#   -> gives a way to use a class exactly as its parent but still each sub class keeps its method as they are

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
             SoftwareEngineer("Liz", 30, 9000, "Senior"),
             Designer("Philip", 27, 7000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)


# Recap:
# Inheritance: ChildClass(BaseClass)
# inherit, extend, override
# super().__init__()
# Polymorphism