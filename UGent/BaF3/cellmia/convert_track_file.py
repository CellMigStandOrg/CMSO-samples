#!/usr/bin/env python

"""\
Convert the tracking file to a tabular data package compliant
format. Also cut unneeded columns.
"""

import sys
import os
import codecs
import argparse


def convert(in_fn, out_fn):
    with codecs.open(in_fn, "r", "iso-8859-1") as f:
        with codecs.open(out_fn, "w", "utf-8") as fo:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fo.write(",".join(line.split("\t")[:4]) + "\n")


def make_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('in_fn', metavar="INPUT_FILE")
    parser.add_argument("-o", "--out-fn", metavar="FILE")
    return parser


def main(argv):
    parser = make_parser()
    args = parser.parse_args(argv[1:])
    if args.out_fn is None:
        args.out_fn = "%s.csv" % os.path.splitext(args.in_fn)[0]
    print "writing to %s" % args.out_fn
    convert(args.in_fn, args.out_fn)


if __name__ == "__main__":
    main(sys.argv)
