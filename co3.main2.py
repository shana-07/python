
from graphics.rectangle import area as rect_area, perimeter as rect_peri
from graphics.circle import area as circ_area, perimeter as circ_peri
from graphics.threeDgraphics.sphere import area as sph_area, perimeter as sph_peri
from graphics.threeDgraphics.cuboid import area as cub_area, perimeter as cub_peri

print("case 2: using selective import")
print("Rectangle Area:",rect_area(8,4))
print("Rectangle perimeter:",rect_peri(8,4))

print("circle Area:",circ_area(5))
print("circle perimeter:",circ_peri(5))


print("cuboid Area:",cub_area(8,4,3))
print("cuboid perimeter:",cub_peri(8,4,3))

print("sphere Area:",sph_area(5))
print("sphere perimeter:",sph_peri(5))
