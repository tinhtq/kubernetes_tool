FROM ubuntu:latest
LABEL authors="tinh"

ENTRYPOINT ["top", "-b"]