import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def angle(self, centroid):
        return (math.atan2(self.y - centroid.y, self.x - centroid.x) + 2.0 * math.pi) % (2.0 * math.pi)

    def distance(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2
