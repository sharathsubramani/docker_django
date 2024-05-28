FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
# COPY requirements.txt /app/
COPY . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
