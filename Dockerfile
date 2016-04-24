FROM python:3.4
WORKDIR /image
COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt
COPY messenger messenger
