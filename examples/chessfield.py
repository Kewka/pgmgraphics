from pgmgraphics.core.Image import Image
from pgmgraphics.core.PGMFile import PGMFile

COLOR_WHITE = 255
WIDTH = 8
HEIGHT = 8

image = Image(WIDTH, HEIGHT)
pgm = PGMFile(image)

for h in range(image.height):
    for w in range(image.width):
        if h % 2 == w % 2:
            image.fill_pixel(w, h, COLOR_WHITE)

pgm.save('chessfield.pgm')
