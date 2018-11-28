FROM tensorflow/tensorflow:latest-py3

ADD . /biomedicus
WORKDIR /biomedicus

RUN pip install --upgrade pip setuptools-scm

RUN pip install .

WORKDIR /biomedicus_data/
