from project import Project
import csv
import click

def write_data_to_csv(csv_filename, data):
    with open(csv_filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def validate_option(ctx, param, value):
    if value is None:
        raise click.BadParameter('You need to provide "%s" option' % param.name)
    return value

@click.command()
@click.option('--project', callback=validate_option, help='Name of the project to parse')
@click.option('--output', callback=validate_option, help='Name of the output CSV file')
def main(project, output):
    p = Project()
    p.read_data_from_xml(project)

    number_of_gcps = len(p.gcps)
    area_covered_by_gcps = p.gcps.polygon().area
    processing_area = p.processing_area.area
    ratio = float(area_covered_by_gcps) / processing_area

    data = [[number_of_gcps, area_covered_by_gcps, processing_area, ratio]]
    write_data_to_csv(output, data)


if __name__ == "__main__":
    main()
