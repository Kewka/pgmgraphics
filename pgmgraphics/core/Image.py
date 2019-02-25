class Image:
    """
    This is class for containing image data.

    Parameters:
        width (int): The image width.
        height (int): The image height.
        background (int): The default pixel color (0-255). Default is 0.
    """

    def __init__(self, width: int, height: int, background: int = 0):
        self.__width = width
        self.__height = height
        self.pixels = [
            [background for w in range(width)] for h in range(height)
        ]

    @property
    def size(self):
        """Returns a tuple consisting of the width and height of the image."""
        return (self.width, self.height)

    @property
    def width(self):
        """Returns the width of the image."""
        return self.__width

    @property
    def height(self):
        """Returns the height of the image."""
        return self.__height

    def fill_pixel(self, x: int, y: int, color: int):
        """Fills a pixel at (x, y) with the specified color."""
        if x >= self.width or y >= self.height:
            return

        self.pixels[y][x] = color
