FROM ubuntu:20.04

RUN apt-get update && apt-get install -y net-tools util-linux python3-pip

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "devopsfetch.py"]
