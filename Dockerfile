FROM ubuntu:latest

MAINTAINER Your Name "samikshaj@cybage.com"

RUN apt-get update -y && \
    apt-get install -y && \ 
    apt-get install python-pip -y && \ 
    apt-get install python-dev -y && \ 
    apt-get install build-essential -y && \
    apt-get install libmysqlclient-dev -y && \
#    apt-get install libpcap-dev libpq-dev -y && \
    apt-get install mysql-server -y && \
    pip install Flask && \
    pip install flask-mysqldb 
#    pip install mysql-python
    
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8086

CMD ["python", "app.py"]

#FROM ubuntu:latest

#RUN apt-get update -y

#RUN apt-get install -y python-pip python-dev build-essential \
    #libmysqlclient-dev && \
   # pip install Flask && \
  #  pip install mysql-python && \	
 #   pip install flask-mysqldb

#COPY . /app

#WORKDIR /app

#RUN pip install -r requirements.txt

#EXPOSE 8086

#ENTRYPOINT ["python"]

#CMD ["app.py"]

