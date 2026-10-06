class Cars:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(self.model)
        print(self.year)
        print(self.color)

    def car_start(self):
        print("The car is started")

# object creation
car1 = Cars("Toyota", 2026, "black")

car1.display()
car1.car_start()
