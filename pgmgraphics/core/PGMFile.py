from pgmgraphics.core.Image import Image


class PGMFile:
    def __init__(self, image: Image):
        self.__image = image

    def save(self, filename: str):
        width, height = self.__image.get_sizes()

        with open(filename, 'wb') as f:
            f.write(b'P2\n')
            f.write(b'%d %d\n' % (width, height))
            f.write(b'255\n')

            for h in range(height):
                for w in range(width):
                    f.write(b'%d ' % self.__image.pixels[h][w])

                f.write(b'\n')
