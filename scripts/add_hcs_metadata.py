import sys
import argparse
import xml.dom.minidom as minidom


WELL_MAP = {
    (1, 1): "9I5TT808_F00000010.tif",
    (2, 1): "9I5TT808_F00000011.tif",
    (3, 1): "9I5TT808_F00000012.tif",
    (4, 1): "9I5TT808_F00000013.tif",
    (1, 3): "9I5TT808_F00000014.tif",
    (2, 3): "9I5TT808_F00000015.tif",
    (3, 3): "9I5TT808_F00000016.tif",
    (4, 3): "9I5TT808_F00000017.tif",
    (1, 5): "9I5TT808_F00000018.tif",
    (2, 5): "9I5TT808_F00000019.tif",
    (3, 5): "9I5TT808_F00000020.tif",
    (4, 5): "9I5TT808_F00000021.tif",
}
INDENT = 3 * " "


def map_image_names(doc):
    m = {}
    for node in doc.getElementsByTagName("Image"):
        attr = dict(node.attributes.items())
        m[attr["Name"]] = attr["ID"]
    return m


def add_wells(doc, plate, img_map):
    for (row, col), fn in sorted(WELL_MAP.iteritems()):
        try:
            img_id = img_map[fn]
        except KeyError:
            continue
        well_id = "Well:%d:%d" % (row, col)
        image_ref = doc.createElement("ImageRef")
        image_ref.setAttribute("ID", img_id)
        well_sample = doc.createElement("WellSample")
        well_sample.setAttribute("ID", "%s:0" % well_id)
        well_sample.appendChild(image_ref)
        well = doc.createElement("Well")
        well.setAttribute("ID", well_id)
        well.setAttribute("Row", "%d" % row)
        well.setAttribute("Column", "%d" % col)
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
