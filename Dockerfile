FROM alpine

RUN apk update
RUN apk add python3

ADD . /opt/xip

WORKDIR /opt/xip

ENTRYPOINT ["python3", "xip.py"]
CMD ["--help"]
