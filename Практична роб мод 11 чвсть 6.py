# Завдання 1
# Використовуючи поняття множинного успадкування,
# створіть клас «Коло, поміщене в квадрат».

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class CircleInSquare(Circle, Square):
    def __init__(self, radius):
        Square.__init__(self, radius * 2)
        Circle.__init__(self, radius)

    def remaining_area(self):
        return self.area() - Square.area(self)


radius = 5
circle_in_square = CircleInSquare(radius)
print("Площа круга:", circle_in_square.area())
print("Площа квадрата:", circle_in_square.area())

