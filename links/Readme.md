Links
-----

This folder contain several proposals to represent and express the concept of
links in CMSO datasets.

The data used to represent a CMSO fileset is the following:

-   the file representing the acquired data is a [sample OME-TIFF fileset](http://downloads.openmicroscopy.org/images/OME-TIFF/2016-06/companion/)
    containing 5 TIFF files and a companion OME-XML file
-   the derived results are tabular data packages generated from a TrackMate XML file using the data package converter tools in this repository.


There are currently three (non-exclusive) proposals for modelling the links
between different sets of files:

-   the simplest proposal is to express links between acquisition and derived
    data in an implicit manner i.e. use file or folder naming convention. The
    [implicit_links_1](implicit_links_1) example stores the acquisition data
    under a folder called ``images`` and the various derived data under folders
    named ``results1``, ``results2``. The [implicit_links_2](implicit_links_2)
    proposal stores both acquisition and derived data under the top-level folder and uses convention on the filenames of the derived data i.e.
    ``results1.json``, ``results2.json``

-   a more advanced proposal is to express these links between acquisition and
    derived data in an explicit manner. Two proposal would allow to express
    these in the OME metadata using Structured Annotations. A complex fileset
    like a data package can be represented by a list of relative paths using
    either a `MapAnnoation` as in the
    [ome_links_1](ome_links_1/multifile.companion.ome) example or an
    `XMLAnnotation` as in the
    [ome_links_2](ome_links_2/multifile.companion.ome) example
