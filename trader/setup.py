#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip
from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt',
                                  session=pip.download.PipSession)
install_reqs = [str(ir.req) for ir in install_reqs]

dev_reqs = parse_requirements('dev-requirements.txt',
                              session=pip.download.PipSession)
dev_reqs = [str(ir.req) for ir in dev_reqs]


setup(
    name="trader",
    version="0.1",
    description="TODO",
    author='Fintx Group',
    author_email='yao.ntno@gmail.com',
    url='TODO',
    license="TODO",
    packages=find_packages(),
    setup_requires=[
        "pip-tools"
        ],
    install_requires=install_reqs,
    extras_require={
        'dev': dev_reqs,
    }
)
