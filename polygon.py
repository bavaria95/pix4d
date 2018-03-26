import math
from point import Point

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.vertices):
            i = self.i
            self.i += 1
            return self.vertices[i]

        raise StopIteration

    def __str__(self):
        s = ""
        for v in self.vertices:
            s += "%s " % v
        return "[ %s]" % s

    def __getitem__(self, item):
        return self.vertices[item]
