# Завдання 2
# Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
# «Колеса», «Двигун», «Двері» та ін
class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

car = Car(number_of_wheels=4, horsepower=200, number_of_doors=4)
print("Кількість коліс:", car.number_of_wheels)
print("Потужність двигуна:", car.horsepower)
print("Кількість дверей:", car.number_of_doors)
