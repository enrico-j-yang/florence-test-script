# -*- coding: utf-8 -*-

import sys
import logging

sys.path.append("../..")

from common.test_result import TestResult


class ActualResult(object, TestResult):
    ser = None
    dist = {}

    def __init__(self):
        super(ActualResult, self).__init__()

    def set_value(self, key, value):
        self.dist[key] = value

    def mock_value(self, key, value):
        self.set_value(key, value)

    def get_value(self, key):
        # read test command to serial port
        logging.info("SerialRead:"+key)
        return self.dist[key]
