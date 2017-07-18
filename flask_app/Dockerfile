FROM ubuntu:16.04
MAINTAINER Prashant Bana "prashantsinghbana673@gmail.com"
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "database.py", "app.py" ]
ENV DEBIAN_FRONTEND teletype
