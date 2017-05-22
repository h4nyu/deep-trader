FROM python:3.5-slim

MAINTAINER Xinyaun Yao <yao.xinyuan@canon.co.jp>

RUN apt-get update && apt-get install -y \
    gcc \
    make

ARG user
ARG uid
ARG gid
RUN echo "${user}, ${uid}, ${gid}"
RUN addgroup --gid ${gid} ${user} 
RUN adduser --uid ${uid} --gid ${gid} --disabled-password ${user} --gecos "" 

RUN pip install cython
RUN pip install pip-tools

WORKDIR /deep-trader
ADD ./requirements.txt /deep-trader
ADD ./dev-requirements.txt /deep-trader
ADD ./Makefile /deep-trader
RUN make sync_package

ADD ./ /deep-trader
RUN pip install -e .[dev]

USER ${user}
CMD ["/bin/bash"]
