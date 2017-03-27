FROM openmicroscopy/ome-files-jupyter

USER root
RUN pip install datapackage
RUN pip install jsontableschema
RUN pip install jsontableschema-pandas
RUN pip install pandas
RUN pip install seaborn
RUN pip install tabulator
RUN pip install xlrd
