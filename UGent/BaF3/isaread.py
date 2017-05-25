"""\
This is just a quick way to read text from an ISA investigation
file. The dataset should be read with isatools.io.isatab_parser from
https://github.com/ISA-tools/isa-api. However, isa-api is Python 3 only,
while this is Python 2 and thus can be used with the current version of
ome-files-py.
"""

import csv

# http://isa-specs.readthedocs.io/en/latest/isatab.html
SECTIONS = frozenset([
    "ONTOLOGY SOURCE REFERENCE",
    "INVESTIGATION",
    "INVESTIGATION PUBLICATIONS",
    "INVESTIGATION CONTACTS",
    "STUDY",
    "STUDY DESIGN DESCRIPTORS",
    "STUDY PUBLICATIONS",
    "STUDY FACTORS",
    "STUDY ASSAYS",
    "STUDY PROTOCOLS",
    "STUDY CONTACTS",
])


def read_investigation(fn):
    rec = {}
    section = None
    with open(fn) as f:
        reader = csv.reader(f, dialect="excel-tab")
        for row in reader:
            if row[0].startswith("#"):
                continue
            if row[0] in SECTIONS:
                section = {}
                rec[row[0]] = section
            else:
                section[row[0]] = row[1:]
    return rec
