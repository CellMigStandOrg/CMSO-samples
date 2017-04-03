FROM openmicroscopy/ome-files-jupyter:0.1.0

USER root
RUN pip install datapackage
RUN pip install jsontableschema
RUN pip install jsontableschema-pandas
RUN pip install pandas
RUN pip install seaborn
RUN pip install tabulator
RUN pip install xlrd

USER jupyter
