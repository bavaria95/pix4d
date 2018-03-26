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

    @property
    def centroid(self):
        cx = float(sum(v.x for v in self.vertices)) / len(self.vertices)
        cy = float(sum(v.y for v in self.vertices)) / len(self.vertices)
        return Point(cx, cy)

    def _sort_vertices_ccw(self):
        return sorted(self.vertices, key=lambda v: v.angle(self.centroid))

    def sort(self):
        '''
            In-place sorting vertices in counter-clockwise order
        '''

        self.vertices = self._sort_vertices_ccw()

    @property
    def area(self):
        '''
            Compute area of a polygon using a shoelace formula
        '''

        vertices = self._sort_vertices_ccw()
        n = len(vertices)
        pol_area = 0.0

        for i in range(n):
            j = (i + 1) % n
            pol_area += vertices[i].x * vertices[j].y
            pol_area -= vertices[j].x * vertices[i].y
        pol_area = abs(pol_area) / 2.0

        return pol_area
