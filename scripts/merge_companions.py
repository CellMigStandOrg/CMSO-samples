import sys
import argparse
import xml.dom.minidom as minidom


INDENT = 3 * " "


# this annotation differs among individual files
def remove_docname(annotations):
    docname_node = None
    for c in annotations.childNodes:
        try:
            key_node = c.getElementsByTagName("Key")[0]
        except AttributeError:
            continue
        if key_node.firstChild.data.strip() == "Document Name":
            docname_node = c
    if docname_node is not None:
        annotations.removeChild(docname_node)


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('fnames', metavar="FILE [FILE]...", nargs="+")
    parser.add_argument("-o", "--out-fn", metavar="FILE", help="output file")
    return parser


def main(argv):
    parser = make_parser()
    args = parser.parse_args(argv[1:])
    args.fnames.sort()
    ref_doc = minidom.parse(args.fnames[0])
    root = ref_doc.firstChild
    annotations = None
    for c in root.childNodes:
        if c.nodeName == "StructuredAnnotations":
            annotations = c
            root.removeChild(c)
    remove_docname(annotations)
    img_count = 0
    for fn in args.fnames[1:]:
        doc = minidom.parse(fn)
        for node in doc.getElementsByTagName("Image"):
            img_count += 1
            node.setAttribute("ID", "Image:%d" % img_count)
            root.appendChild(node)
    root.appendChild(annotations)
    out_doc = minidom.Document()
    out_doc.appendChild(root)
    output = out_doc.toprettyxml(indent=INDENT, encoding=ref_doc.encoding)
    output = "\n".join(_ for _ in output.splitlines() if _.strip())
    if args.out_fn:
        with open(args.out_fn, "w") as fo:
            fo.write(output)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main(sys.argv)
