#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import requests
import csv
from datetime import datetime
from datetime import timedelta
from io import StringIO
from pprint import pprint
import pandas as pd
import numpy as np
import json
from .dao import Dao


class YCollector(Dao):

    """Docstring for Collector. """

    def __init__(self):
        """TODO: to be defined1. """
        pass
        self.api_url = 'https://query.yahooapis.com/v1/public/yql?'
        self.datatable_url = 'store://datatables.org/alltableswithkeys'

    def get_histrical_data(self, symbol, start_date, end_date):
        yql = 'select * from yahoo.finance.historicaldata '\
            + 'where symbol = "{0}" '.format(symbol)\
            + 'and startDate = "{0}" '.format(start_date)\
            + 'and endDate = "{0}"'.format(end_date)

        pyload = {
            'q': yql,
            'format': 'json',
            'env': self.datatable_url
        }

        r = requests.get(self.api_url, params=pyload)
        return r.json()['query']['results']['quote']

    def get_quote(self, symbol):
        yql = 'select * from yahoo.finance.quote '\
            + 'where symbol = "{0}" '.format(symbol)

        pyload = {
            'q': yql,
            'format': 'json',
            'env': self.datatable_url
        }

        r = requests.get(self.api_url, params=pyload)

        return r.json()['query']['results']['quote']
