class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        r = "X:" + str(self.x) + " Y:" + str(self.y)
        return r
