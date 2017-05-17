FROM python:3.5-slim

MAINTAINER Xinyaun Yao <yao.xinyuan@canon.co.jp>

RUN pip install cython

WORKDIR /srv
ADD . /srv
RUN pip install -e .[dev]

CMD ["python", "run.py"]
