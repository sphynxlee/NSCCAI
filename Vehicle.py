class Vehicle:
    def __init__(self, maker, brand, model, year, color):
        self.maker = maker
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def engine_start(self):
        self.engine_status = True

    def engine_stop(self):
        self.engine_status = False

# myCar = Vehicle("Toyota", "Corolla", "LE", 2019, "White")
# print(myCar.maker)

# create a new class called Car that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, maker, brand, model, year, color, doors):
        # call the constructor of the Vehicle class
        super().__init__(maker, brand, model, year, color)
        self.doors = doors

    def open_doors(self):
        print("Doors are now open.")

    def close_doors(self):
        print("Doors are now closed.")

myCar = Car("Toyota", "Corolla", "LE", 2019, "White", 4)
print(myCar.maker)

# create a new class called Motorcycle that inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, maker, brand, model, year, color, engine_type):
        # call the constructor of the Vehicle class
        super().__init__(maker, brand, model, year, color)
        self.engine_type = engine_type

    def wheelie(self):
        print("Doing a wheelie!")

myBike = Motorcycle("Honda", "CBR", "1000RR", 2019, "Red", "Inline 4")
myBike.wheelie()
print(myBike.maker)

# create a new class called Boat that inherits from Vehicle
class Boat(Vehicle):
    def __init__(self, maker, brand, model, year, color, length):
        # call the constructor of the Vehicle class
        super().__init__(maker, brand, model, year, color)
        self.length = length

    def anchor(self):
        print("Anchors away!")

myBoat = Boat("Sea Ray", "Sundancer", "320", 2019, "White", 32)
myBoat.anchor()
print(myBoat.maker)

