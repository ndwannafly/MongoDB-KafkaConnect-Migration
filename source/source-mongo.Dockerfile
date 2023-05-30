FROM mongo:6.0.5

COPY ./source/config-replica-source.js /
COPY ./source/.bashrc /data/db/.bashrc
COPY gen_data.py /
COPY requirements.txt /
RUN mkdir /scratch_space
ADD utils /usr/local/bin
RUN chmod +x /usr/local/bin/cx
RUN chmod +x /usr/local/bin/del
RUN chmod +x /usr/local/bin/kc
RUN chmod +x /usr/local/bin/status
RUN chmod +x /gen_data.py

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y curl
RUN apt-get install -y python3-pip
RUN apt-get install -y nano vim
RUN apt-get install -y bsdmainutils
RUN apt-get install -y kafkacat
RUN apt-get install -y git
RUN apt-get install -y dos2unix

RUN dos2unix /usr/local/bin/*
RUN dos2unix /data/db/.bashrc
RUN pip3 install -r /requirements.txt
# RUN python3 ./gen_data.py
