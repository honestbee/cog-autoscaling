FROM python:3.6-alpine

MAINTAINER Charles Martinot <charles.martinot@honestbee.com>

RUN adduser -h /home/bundle -D bundle

USER root
COPY setup.py requirements.txt /home/bundle/autoscaling/
WORKDIR /home/bundle/autoscaling
RUN pip install -r requirements.txt
COPY autoscaling/*.py /home/bundle/autoscaling/autoscaling/
COPY autoscaling/commands/*.py /home/bundle/autoscaling/autoscaling/commands/
RUN pip install .
