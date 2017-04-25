#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.layers import Split
import pytest


@pytest.fixture()
def split(request):
    return Split()


def test_type(split):
    assert isinstance(split, Split)
