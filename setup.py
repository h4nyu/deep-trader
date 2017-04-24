#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    user_options = [
        ('pytest-args=', 'a', 'Arguments for pytest'),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_target = []
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup_requires = [
    'pytest'
]

tests_require = [
    'pytest-timeout',
    'pytest'
]


setup(
    name="app",
    version="0.1",
    packages=find_packages(),
    cmdclass={'test': PyTest}
)
