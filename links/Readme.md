Links
-----

This folder contain several proposals to represent and express the concept of
links in CMSO datasets.

The data used to represent a CMSO fileset is the following:

-   the file representing the acquired data is a [sample OME-TIFF fileset](http://downloads.openmicroscopy.org/images/OME-TIFF/2016-06/companion/)
    containing 5 TIFF files and a companion OME-XML file
-   the derived results are tabular data packages generated from a TrackMate XML file using the data package converter tools in this repository.


The simplest proposal would be to express links between acquisition and
derived data in an implicit manner i.e. use file or folder naming convention.
For example, the acquisition data can be stored under a folder called
``images`` and the various derived data under folders named ``results1``,
``results2``. Alternatively, both acquisition and derived data could be stored
under a top-level folder and use convention on the filenames of the derived
data i.e. ``results1.json``, ``results2.json``.

A more advanced proposal is to express these links between acquisition and
derived data in an explicit manner. Two proposal would allow to express these
in the OME metadata using Structured Annotations like XMLAnnotation or
MapAnnotation. A complex fileset like a data package can be represented by a
list of relative paths as in the
[multifile.companion.ome](multifile.companion.ome) companion file.
