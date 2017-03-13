import sys
import os
import argparse
import subprocess
import tempfile
import xml.dom.minidom as minidom


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('cname', metavar="COMPANION_NAME")
    parser.add_argument('cuuid', metavar="COMPANION_UUID")
    parser.add_argument('fn', metavar="FILE")
    parser.add_argument('--tiffcomment', metavar="EXEC_FILE",
                        default="tiffcomment",
                        help="path to tiffcomment executable")
    return parser


def main(argv):
    parser = make_parser()
    args = parser.parse_args(argv[1:])
    if not args.cuuid.startswith("urn:uuid:"):
        args.cuuid = "urn:uuid:%s" % args.cuuid
    ome_block = subprocess.check_output([args.tiffcomment, args.fn]).strip()
    doc = minidom.parseString(ome_block)
    node = doc.getElementsByTagName("BinaryOnly")[0]
    node.setAttribute("MetadataFile", os.path.basename(args.cname))
    node.setAttribute("UUID", args.cuuid)
    xml_fn = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix="ome_", suffix=".xml", delete=False
        ) as fo:
            xml_fn = fo.name
            fo.write(doc.toxml())
        subprocess.check_output([args.tiffcomment, "-set", xml_fn, args.fn])
    finally:
        if xml_fn is not None:
            os.remove(xml_fn)


if __name__ == "__main__":
    main(sys.argv)
