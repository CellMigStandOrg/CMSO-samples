FROM openmicroscopy/ome-files-py

RUN pip install datapackage
RUN pip install jsontableschema
RUN pip install jsontableschema-pandas
RUN pip install matplotlib
RUN pip install pandas
RUN pip install seaborn
RUN pip install tabulator
RUN pip install xlrd
RUN pip install jupyter

RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

WORKDIR /notebooks

EXPOSE 8888

COPY run_jupyter /bin/
RUN chmod +x /bin/run_jupyter

CMD ["run_jupyter"]
