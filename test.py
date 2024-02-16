class Car:
    def __init__(self, make, model, year, color,number,engine):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0
        self.number = number
        self.engine = engine

    def drive(self, miles):
        self.mileage += miles
        print(f"The car has driven {miles} miles.")

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage} miles")
        print(f"Number: {self.number}")
        print(f"Engine: {self.engine}")

# Приклад використання класу Car
my_car = Car("Bmw", "328i", 2013, "blue", "AT8182IB", "2.0 TwinTurbo (N24)")
my_car.drive(100)
my_car.drive(50)
my_car.display_info()
