FROM python:3.5-slim


MAINTAINER Xinyaun Yao <yao.xinyuan@canon.co.jp>

RUN apt-get update && apt-get upgrade -y \
    g++ \
    make 

RUN pip install cython
RUN pip install pip-tools
ENV HOME /srv

WORKDIR /srv
ADD ./requirements.txt /srv
ADD ./dev-requirements.txt /srv
ADD ./Makefile /srv
RUN make sync_package
ADD ./ /srv
RUN pip install -e .[dev]
CMD ["python", "run.py"]
