# -*- coding: utf-8 -*-

import sys

sys.path.append("../..")

from common.test_input import TestInput


class HumanInput(object, TestInput):
    def __init__(self):
        super(HumanInput, self).__init__()
