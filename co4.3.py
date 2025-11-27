class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    # Overload <
    def __lt__(self, other):
        return self.area() < other.area()


r1 = Rectangle(10, 4)
r2 = Rectangle(6, 9)

if r1 < r2:
    print("r1 has smaller area than r2")
else:
    print("r1 has larger or equal area compared to r2")
