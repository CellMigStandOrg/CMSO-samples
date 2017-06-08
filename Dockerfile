FROM openmicroscopy/ome-files-jupyter:latest

USER root
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip3 install -r /requirements.txt

USER jupyter
