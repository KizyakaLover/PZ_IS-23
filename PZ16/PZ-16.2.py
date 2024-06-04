class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Figure):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Figure):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 4 * self.width


rectangle = Rectangle(5, 10)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

square = Square(5)
print(f"Square Area: {square.area()}")
print(f"Square Perimeter: {square.perimeter()}")
