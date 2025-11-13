from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere

print("case 1: using normal import")
print("Rectangle Area:",rectangle.area(10,5))
print("Rectangle perimeter:",rectangle.perimeter(10,5))

print("circle Area:",circle.area(7))
print("circle perimeter:",circle.perimeter(7))


print("cuboid Area:",cuboid.area(10,5,4))
print("cuboid perimeter:",cuboid.perimeter(10,5,4))

print("sphere Area:",sphere.area(7))
print("sphere perimeter:",sphere.perimeter(7))
