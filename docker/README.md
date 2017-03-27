```
cd docker
docker build -t cmso-jupyter .
docker run --rm -it -p 8888:8888 cmso-jupyter
```

Use the URL shown in the startup message, including the token, to access the notebook server from your browser.

For persistence, and to use existing notebooks, you can mount a host directory to `/home/jupyter/notebooks` in the container:

```
docker run --rm -it -p 8888:8888 -v /host/dir:/home/jupyter/notebooks cmso-jupyter
```
