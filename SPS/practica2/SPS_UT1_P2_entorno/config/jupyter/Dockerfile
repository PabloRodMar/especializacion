# Jupyter con las librerías de la práctica (mismas versiones de Pandas que en Colab)
FROM python:3.12-slim
RUN pip install --no-cache-dir jupyterlab==4.2.5 pandas==2.2.3 pyarrow==17.0.0 hdfs==2.7.3
WORKDIR /trabajo
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", \
     "--IdentityProvider.token=", "--ServerApp.password=", "--ServerApp.root_dir=/trabajo"]
