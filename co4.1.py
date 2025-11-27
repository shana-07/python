class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Create objects
r1 = Rectangle(10, 5)
r2 = Rectangle(7, 8)

print("Area of r1:", r1.area())
print("Area of r2:", r2.area())

# Compare
if r1.area() > r2.area():
    print("Rectangle r1 has larger area.")
elif r1.area() < r2.area():
    print("Rectangle r2 has larger area.")
else:
    print("Both rectangles have equal area.")
