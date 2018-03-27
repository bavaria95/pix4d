from project import Project
import csv

def write_data_to_csv(csv_filename, data):
    with open(csv_filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

p = Project()
p.read_data_from_xml('2.p4d')

number_of_gcps = len(p.gcps)
area_covered_by_gcps = p.gcps.polygon().area
processing_area = p.processing_area.area
ratio = float(area_covered_by_gcps) / processing_area

data = [[number_of_gcps, area_covered_by_gcps, processing_area, ratio]]
write_data_to_csv('out.csv', data)
