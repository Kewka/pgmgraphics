from pgmgraphics.core.Image import Image
from pgmgraphics.core.PGMFile import PGMFile
import math

COLOR_WHITE = 255
WIDTH = 128
HEIGHT = 128
RADIUS = 48

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2


image = Image(WIDTH, HEIGHT)
pgm = PGMFile(image)

width, height = image.get_sizes()


for angle in range(int(math.degrees(math.pi * 2))):
    x = CENTER_X + RADIUS * math.cos(math.radians(angle))
    y = CENTER_Y + RADIUS * math.sin(math.radians(angle))
    image.fill_pixel(int(x), int(y), COLOR_WHITE)

pgm.save('circle.pgm')
