# -*- coding: utf-8 -*-
# Need virtualenv
.PHONY: all clean build rebuild

all: env build
	@echo "build finished..."

build:env
	pip-compile  dev-requirements.in
	pip-compile dev-requirements.in
	pip-sync requirements.txt dev-requirements.txt

env:
	pip install pip-tools
