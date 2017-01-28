Links
-----

This folder contain several proposals to represent and express the concept of
links in CMSO datasets.

The data used to represent a CMSO fileset is the following:

-   the image acquisition data is a[sample OME-TIFF fileset](http://downloads.openmicroscopy.org/images/OME-TIFF/2016-06/companion/)
    containing 5 TIFF files and a companion OME-XML file
-   the derived results are tabular data packages generated from a TrackMate XML file using the data package converter tools in this repository


There are currently three (non-exclusive) proposals for modelling the links
between different sets of files:

-   the [simplest proposal](proposal1) is to rely on naming conventions to
    express relationships, e.g. folder naming conventions like ``images``,
    ``results``

-   a second proposal is to store these links in the OME-XML metadata using the
    OME structured annotations either as [map annotations](proposal2) or
    [XML annotations](proposal3).
