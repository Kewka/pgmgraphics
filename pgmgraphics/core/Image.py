class Image:
    def __init__(self, width: int, height: int, background: int = 0):
        self.__width = width
        self.__height = height
        self.pixels = [
            [background for w in range(width)] for h in range(height)]

    def get_sizes(self):
        return (self.__width, self.__height)

    def fill_pixel(self, x: int, y: int, color: int):
        if x >= self.__width or y >= self.__height:
            return

        self.pixels[y][x] = color
