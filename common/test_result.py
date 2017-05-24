# -*- coding: utf-8 -*-
import logging


class TestResult:
    dist = {}
    mock_enable = False

    def __init__(self, mock_enable=False):
        self.mock_enable = mock_enable
        if self.mock_enable:
            logging.debug('TestResult enable')
        else:
            logging.debug('TestResult')

    def set_value(self, key, value):
        self.dist[key] = value

    def mock_value(self, key, value):
        if self.mock_enable:
            self.set_value(key, value)

    def get_value(self, key):
        return self.dist[key]
