class Lamp:
    def __init__(self, type):
        self.type = type

    def on(self):
        print(f"\tTurning ON {self.type} lamp")

    def off(self):
        print(f"\tTurning OFF {self.type} lamp")

class Engine:
    def __init__(self, make):
        self.make = make

    def start(self):
        print(f"\tStarting {self.make} engine")

    def stop(self):
        print(f"\tStopping {self.make} engine")

    def run(self):
        print(f"\tRunning {self.make} engine")

class Car:
    def __init__(self, make, lamp_type):
        self.make = make
        self.engine = Engine(make)
        self.lamp = Lamp(lamp_type)

    def drive(self):
        print(f"Driving {self.make} car")
        self.engine.start()
        self.lamp.on()
        self.engine.run()

    def park(self):
        print(f"Parking {self.make} car")
        self.engine.stop()
        self.lamp.off()


car1 = Car("Volvo", "LED")
car2 = Car("Nissan", "Bulb")
car3 = Car("Honda", "Halogen")

car1.drive()
car2.drive()
car1.park()
car2.park()

car3.drive()
car3.park()

car1.drive()