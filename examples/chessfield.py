from pgmgraphics.core.Image import Image
from pgmgraphics.core.PGMFile import PGMFile

COLOR_WHITE = 255
WIDTH = 16
HEIGHT = 16

image = Image(WIDTH, HEIGHT)
pgm = PGMFile(image)

width, height = image.get_sizes()

for h in range(height):
    for w in range(width):
        if h % 2 == w % 2:
            image.fill_pixel(w, h, COLOR_WHITE)

pgm.save('chessfield.pgm')
