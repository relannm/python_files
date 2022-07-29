class Parrot:
    # a class is a blueprint (naming convention starter with uppercase)

    # class attribute can be used by Class and each instance/object
    species = "bird"

    # *** ALL FUNCTIONS INSIDE THE CLASS NEED self argument ***
    # *** self acts as the instance of the class
    # *** except when function is used only within the class

    def __init__(self, name, age):
        # instance attributes are tied to specific instance/object
        self.name = name
        self.age = age

    # instance method
    def sing(self):
        """ Function for making parrot sing """
        print(f"{self.name} is singing... Tweet tweet!")

    def fly(self, direction="unknown"):
        """ Function for making parrot fly """
        print(f"{self.name} is flying toward {direction}")

    # dunder method
    def __str__(self):
        info = f"name = {self.name}, age = {self.age}"
        return info

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    #adding decorator is used to make the function accessible by instance and class
    @staticmethod
    def staticmethodtest():
        print("Testing only")


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
wee = Parrot("Woo", 15)

print("Blu is a " + blu.species)
print("Woo is a " + woo.species)

print(blu.name, blu.age)

blu.sing()
woo.sing()

blu.fly("north")
woo.fly()

print(blu)
print(woo)

print(blu == woo)
# if statement below is called without adding __eq__ it returns false
# because the two instances resides in different memory location
print(wee == woo)

print(Parrot.staticmethodtest())
print(blu.staticmethodtest())