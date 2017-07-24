#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import requests
import csv
from datetime import datetime
from datetime import timedelta
from io import StringIO
from pprint import pprint
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import numpy as np
import json


class Dao(metaclass=ABCMeta):

    """Docstring for Dao. """

    def __init__(self):
        """TODO: to be defined1. """
        metaclass = ABCmeta.__init__(self)

    @abstractmethod
    def get_histrical_data(self, symbol, start_date, end_date):
        pass

    @abstractmethod
    def get_quote(self, symbol):
        pass
