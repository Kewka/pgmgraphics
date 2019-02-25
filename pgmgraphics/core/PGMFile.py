from pgmgraphics.core.Image import Image


class PGMFile:
    """
    This is class for containing PGM file data.

    Parameters:
        image (Image): The image.
    """

    def __init__(self, image: Image):
        self.__image = image

    def save(self, filename: str):
        """Saves the file with the specified name."""
        with open(filename, 'wb') as f:
            f.write(b'P2\n')
            f.write(b'%d %d\n' % (self.__image.width, self.__image.height))
            f.write(b'255\n')

            for h in range(self.__image.height):
                for w in range(self.__image.width):
                    f.write(b'%d ' % self.__image.pixels[h][w])

                f.write(b'\n')
