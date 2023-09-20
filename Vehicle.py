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

myCar = Vehicle("Toyota", "Corolla", "LE", 2019, "White")
print(myCar.maker)

#