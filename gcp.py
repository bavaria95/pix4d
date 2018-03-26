from point import Point

class GCP(Point):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label
