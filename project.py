import xml.etree.ElementTree as ET

from point import Point
from gcp import GCP
from gcps import GCPs
from processing_area import ProcessingArea


class Project:
    def __init__(self):
        pass

    def read_data_from_xml(self, filename):
        self.filename = filename
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()

        self._fill_data_from_xml()

    def _fill_data_from_xml(self):
        self.processing_area = self._read_processing_area()
        self.gcps = self._read_gcps()

    def _read_processing_area(self):
        allowed_processing_area_types = set(('geoCoord2D', 'geoCoord3D'))
        try:
            pa_el = self.root.find('./inputs/processingArea')
            vertices = []
            for p in pa_el.getchildren():
                if p.tag in allowed_processing_area_types:
                    vertices.append(Point(float(p.get('x')), float(p.get('y'))))
        except AttributeError:
            vertices = []

        return ProcessingArea(vertices)

    def _read_gcps(self):
        try:
            gcps_el = self.root.find('./inputs/gcps')
            gcps_points = [GCP(float(p.get('x')), float(p.get('y')), p.get('label'))
                           for p in gcps_el.getchildren()]
        except AttributeError:
            gcps_points = []

        return GCPs(gcps_points)

    def draw(self):
        '''
            Drawing very primitive doodle of the project
        '''

        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.patches
        from matplotlib.collections import PatchCollection

        fig, ax = plt.subplots()

        # plotting dots for processing area points
        plt.plot([v.x for v in self.processing_area],
                  [v.y for v in self.processing_area],
                  'bo')

        # creating polygon for processing area
        pa_array = [(v.x, v.y) for v in self.processing_area]
        pa_polygon = matplotlib.patches.Polygon(pa_array)

        # plotting points for GCPs
        plt.plot([p.x for p in self.gcps],
                  [p.y for p in self.gcps],
                  'rx')

        # computing convex hull and creating polygon for it
        convex_hull = self.gcps.convex_hull()
        ch_array = [(p.x, p.y) for p in convex_hull]
        ch_polygon = matplotlib.patches.Polygon(ch_array)


        patches = [pa_polygon, ch_polygon]
        p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

        colors = 100*np.random.rand(len(patches))
        p.set_array(np.array(colors))

        ax.add_collection(p)

        plt.show()
