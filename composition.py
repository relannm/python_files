# COMPOSITION
#   -> represented by "HAS A" relationship
#   -> ex: Employee "HAS A" Salary

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()

e1 = Employee('Max', 25, 1000, 100)
print(e1.total_salary())