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

EXPOSE 8888

COPY run_jupyter /bin/
RUN chmod +x /bin/run_jupyter

RUN useradd -m jupyter
USER jupyter
ENV HOME /home/jupyter
RUN mkdir -p -m 700 ${HOME}/.jupyter/ && \
  echo "c.NotebookApp.ip = '*'" >> ${HOME}/.jupyter/jupyter_notebook_config.py

WORKDIR ${HOME}/notebooks

CMD ["run_jupyter"]
