FROM jupyter/base-notebook:latest

USER root

# graphviz binary (the Python package wraps this) + Java for HermiT reasoner
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        graphviz \
        default-jre-headless && \
    rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
