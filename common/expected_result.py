# -*- coding: utf-8 -*-

import sys

sys.path.append("../..")

from common.test_result import TestResult


class ExpectedResult(TestResult):
    def __init__(self):
        super(ExpectedResult, self).__init__()
