FROM python:3.5-slim

MAINTAINER Xinyaun Yao <yao.xinyuan@canon.co.jp>

RUN pip install cython

WORKDIR /srv
ADD . /srv
RUN pip install -e .[dev]

CMD ["python", "run.py"]
||||||| merged common ancestors
=======
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

WORKDIR /deep_trader
ADD ./requirements.txt /deep_trader
ADD ./dev-requirements.txt /deep_trader
ADD ./Makefile /deep_trader
RUN make sync_package

ADD ./ /deep_trader
RUN pip install -e .[dev]

USER ${user}
CMD ["python", "run.py"]
>>>>>>> feature/docker
