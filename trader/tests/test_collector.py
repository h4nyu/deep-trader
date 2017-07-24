#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datetime import datetime
from datetime import timedelta
from deep_trader.collector import GCollector


@pytest.fixture
def collector():
    return GCollector()


def test_get_error_historical_quote(collector):
    c = collector
    hist_data = c.get_histrical_data(
        3371, datetime.now() - timedelta(days=2), datetime.now(), 10)
    print(hist_data)
    assert hist_data is None
