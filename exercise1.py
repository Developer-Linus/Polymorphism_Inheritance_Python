class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def calculate_area(self, lenght, width):
        return lenght*width
rectangle1 = Rectangle()
print(rectangle1.calculate_area(10,20))