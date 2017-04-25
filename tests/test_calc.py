#!/usr/bin/env python
# -*- coding: utf-8 -*-

import app.calc


def test_add():
    assert app.calc.add(1, 2) == 4
