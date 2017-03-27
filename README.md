# Samples

Samples received from CMSO to test initial development of data formats and APIs.

Folders containing sample files are named after institutes that generated the data. 


## Notebooks

In order to execute the notebooks, you can build the Dockerfile stored in the
top-level of this repository


    docker build -t cmso-jupyter .
    docker run --rm -it -p 8888:8888 cmso-jupyter

Use the URL shown in the startup message, including the token, to access the
notebook server from your browser.

For persistence, and to use existing notebooks, you can mount a host directory
to `/home/jupyter/notebooks` in the container:

    docker run --rm -it -p 8888:8888 -v $(pwd):/home/jupyter/notebooks cmso-jupyter
