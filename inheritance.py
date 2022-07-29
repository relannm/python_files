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

# to create and instance of SoftwareEngineer (child) class, it needs the attributes of parent class
se = SoftwareEngineer("Max", 25, 6000, "Junior")

print("Software Engineer")
print(se.name, se.age)
se.work()
print(se.level)
se.debug()

print("\n\nDesigner")
d = Designer("Philip", 27, 7000)
print(d.name, d.age)
d.work()
d.draw()