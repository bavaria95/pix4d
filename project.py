import xml.etree.ElementTree as ET
from point import Point
from gcp import GCP
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
        try:
            pa_el = self.root.find('./inputs/processingArea')
            vertices = [Point(float(p.get('x')), float(p.get('y')))
                        for p in pa_el.getchildren()]
        except AttributeError:
            return ProcessingArea([])

        return ProcessingArea(vertices)

    def _read_gcps(self):
        try:
            gcps_el = self.root.find('./inputs/gcps')
            return [GCP(float(p.get('x')), float(p.get('y')), p.get('label'))
                 for p in gcps_el.getchildren()]
        except AttributeError:
            return []
