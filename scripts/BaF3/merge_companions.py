import sys
import argparse
import xml.dom.minidom as minidom


INDENT = 3 * " "


def nontext_children(node):
    for c in node.childNodes:
        if not c.nodeType == minidom.Node.TEXT_NODE:
            yield c


def annotations_as_map(annotations):
    m = {}
    for xml_ann in nontext_children(annotations):
        ann_value = nontext_children(xml_ann).next()
        orig_md = nontext_children(ann_value).next()
        key = orig_md.getElementsByTagName("Key")[0]
        value = orig_md.getElementsByTagName("Value")[0]
        m[key.firstChild.data.strip()] = value.firstChild.data.strip()
    return m


def equalize_annotations(annotations, diff_ann_keys):
    if not diff_ann_keys:
        return
    to_remove = []
    for c in annotations.childNodes:
        try:
            key_node = c.getElementsByTagName("Key")[0]
        except AttributeError:
            continue
        if key_node.firstChild.data.strip() in diff_ann_keys:
            to_remove.append(c)
    for n in to_remove:
        annotations.removeChild(n)


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
    ref_ann_map = annotations_as_map(annotations)
    diff_ann_keys = set()
    img_count = 0
    for fn in args.fnames[1:]:
        doc = minidom.parse(fn)
        for node in doc.getElementsByTagName("Image"):
            img_count += 1
            node.setAttribute("ID", "Image:%d" % img_count)
            root.appendChild(node)
        ann = doc.getElementsByTagName("StructuredAnnotations")[0]
        ann_map = annotations_as_map(ann)
        assert set(ann_map) == set(ref_ann_map)
        for k, v in ref_ann_map.iteritems():
            if ann_map[k] != v:
                diff_ann_keys.add(k)
    print "removing annotations with diff values:", sorted(diff_ann_keys)
    equalize_annotations(annotations, diff_ann_keys)
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
