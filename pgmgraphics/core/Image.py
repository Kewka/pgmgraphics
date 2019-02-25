class Image:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pixels = [[0 for w in range(width) ] for h in range(height)]
