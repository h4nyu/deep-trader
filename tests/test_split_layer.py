#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.layers import Split

class TestSplit(object):

    def pytest_funcarg__split(request):
        return Split()

    def test_type(self, split):
        assert isinstance(split, Split)
