class Parrot:
    #a class is a blueprint (naming convention starter with uppercase)

    #class attribute can be used by Class and each instance/object
    species = "bird"

    def __init__(self, name, age):
        # instance attributes are tied to specific instance/object
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a " + blu.species)
print("Woo is a " + woo.species)

print(blu.name, blu.age)