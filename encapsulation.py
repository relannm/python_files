# ENCAPSULATION
#   -> mechanism of hiding of data implementation
#   -> instance variable are kept private/hidden
#   -> outside access can be done by using public methods (setters / getters)


class SoftwareEngineer():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # private variable/attribute -> by naming convention/practice starts with "_"
        # variable name: _x is called "protected" while __x is called "private"
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        # private function
        self._num_bugs_solved += 1

    def get_salary(self):
        return self._salary

    def set_salary(self, base_value):
        # check value
        #if value < 1000:
        #    self._salary = 1000
        #elif value > 2000:
        #    self._salary = 2000
        #else:
        #    self._salary = value
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return  base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se = SoftwareEngineer("Max", 25)
print(se.name, se.age)
print(se._salary)   # technically in Python, the private functions can be accessed outside (unless it starter with "__")

print("\n *** After using setters and getters -> should be the only way to access outside the class (encapsulation)")
print("\n *** After using setters and getters -> should be the only way to access outside the class (encapsulation)")
se.set_salary(6000)
print(se.get_salary())

for i in range(100):
    se.code()

se.set_salary(6000)
print(se.get_salary())

