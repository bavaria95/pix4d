from gcp import GCP
import functools

epsilon = 10e-8
COUNTER_CLOCKWISE, CLOCKWISE, COLINEAR = (1, -1, 0)

class GCPs:
    def __init__(self, gcps=[]):
        self.gcps = gcps

    def __len__(self):
        return len(self.gcps)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.gcps):
            i = self.i
            self.i += 1
            return self.gcps[i]

        raise StopIteration

    def __getitem__(self, item):
        return self.gcps[item]

    def __delitem__(self, key):
        del self.gcps[key]

    def append(self, item):
        self.gcps.append(item)

    @staticmethod
    def _orient(p, q, r):
        orientation = (q.x - p.x) * (r.y - p.y) - (r.x - p.x) * (q.y - p.y)
        if abs(orientation) <= epsilon:
            return COLINEAR
        elif orientation > epsilon:
            return COUNTER_CLOCKWISE
        else:
            return CLOCKWISE

    @staticmethod
    def _keep_left(hull, r):
        while len(hull) > 1 and GCPs._orient(hull[-2], hull[-1], r) != COUNTER_CLOCKWISE:
            hull.pop()
        hull.append(r)
        return hull

    def convex_hull(self):
        '''
            Returns points on convex hull of an array of points in CCW order
        '''

        points = self.gcps
        # Find the point with lowest y coordinate (and lowest x coordinate
        # if there are more than one point with lowest y coordinate)
        lowest_Y = GCP(float("inf"), float("inf"), None)
        for point in points:
            if point.y < lowest_Y.y - epsilon:
                lowest_Y = point
            elif abs(point.y - lowest_Y.y) <= epsilon and point.x < lowest_Y.x:
                lowest_Y = point

        # Comparator used to compare 2 points while sorting by angle
        def comparator(p1, p2):
            orientation = GCPs._orient(lowest_Y, p1, p2)
            if orientation == COLINEAR:
                dist = lowest_Y.distance(p1) - lowest_Y.distance(p2)
                if abs(dist) <= epsilon:
                    return 0
                elif dist > epsilon:
                    return 1
                else:
                    return -1
            else:
                return -orientation

        points = sorted(points, key=functools.cmp_to_key(comparator))
        return functools.reduce(GCPs._keep_left, points, [])
