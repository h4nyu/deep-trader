# -*- coding: utf-8 -*-
# Need virtualenv
.PHONY: all clean build database pip restore

all: install
	@echo "build finished..."

install:
	pip install -e .

install_dev:
	pip install -e .[dev]

test:
	py.test

fetch_package:
	pip-compile requirements.in
	pip-compile dev-requirements.in

sync_package:
	pip-sync requirements.txt dev-requirements.txt




			
