import sys
import argparse
import xml.dom.minidom as minidom

N_ROWS = 6
N_COLUMNS = 8
WELL_MAP = {
    (1, 1): ("9I5TT808_F00000010.tif", "p190,control"),
    (2, 1): ("9I5TT808_F00000011.tif", "p190,control"),
    (3, 1): ("9I5TT808_F00000012.tif", "p190,y27632"),
    (4, 1): ("9I5TT808_F00000013.tif", "p190,y27632"),
    (1, 3): ("9I5TT808_F00000014.tif", "p210,control"),
    (2, 3): ("9I5TT808_F00000015.tif", "p210,control"),
    (3, 3): ("9I5TT808_F00000016.tif", "p210,y27632"),
    (4, 3): ("9I5TT808_F00000017.tif", "p210,y27632"),
    (1, 5): ("9I5TT808_F00000018.tif", "p210m,control"),
    (2, 5): ("9I5TT808_F00000019.tif", "p210m,control"),
    (3, 5): ("9I5TT808_F00000020.tif", "p210m,y27632"),
    (4, 5): ("9I5TT808_F00000021.tif", "p210m,y27632"),
}
INDENT = 3 * " "


def map_image_names(doc):
    m = {}
    for node in doc.getElementsByTagName("Image"):
        attr = dict(node.attributes.items())
        m[attr["Name"]] = attr["ID"]
    return m


def add_wells(doc, plate, img_map):
    for (row, col), (fn, well_type) in sorted(WELL_MAP.iteritems()):
        well_idx = row * N_COLUMNS + col
        try:
            img_id = img_map[fn]
        except KeyError:
            continue
        image_ref = doc.createElement("ImageRef")
        image_ref.setAttribute("ID", img_id)
        well_sample = doc.createElement("WellSample")
        # only one WellSample per Well
        well_sample.setAttribute("ID", "WellSample:%d:%d:0" % (row, col))
        well_sample.setAttribute("Index", "%d" % well_idx)
        well_sample.appendChild(image_ref)
        well = doc.createElement("Well")
        well.setAttribute("ID", "Well:%d:%d" % (row, col))
        well.setAttribute("Row", "%d" % row)
        well.setAttribute("Column", "%d" % col)
        well.setAttribute("Type", well_type)
        well.appendChild(well_sample)
        plate.appendChild(well)


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('in_fn', metavar="OME_XML_FILE")
    parser.add_argument("-o", "--out-fn", metavar="FILE", help="output file")
    return parser


def main(argv):
    parser = make_parser()
    args = parser.parse_args(argv[1:])
    doc = minidom.parse(args.in_fn)
    img_map = map_image_names(doc)
    plate = doc.createElement("Plate")
    plate.setAttribute("ID", "Plate:0")
    plate.setAttribute("Name", "Ba/F3")
    plate.setAttribute("Rows", "%d" % N_ROWS)
    plate.setAttribute("Columns", "%d" % N_COLUMNS)
    add_wells(doc, plate, img_map)
    root = doc.firstChild
    root.appendChild(plate)
    output = doc.toprettyxml(indent=INDENT, encoding=doc.encoding)
    output = "\n".join(_ for _ in output.splitlines() if _.strip())
    if args.out_fn:
        with open(args.out_fn, "w") as fo:
            fo.write(output)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main(sys.argv)
