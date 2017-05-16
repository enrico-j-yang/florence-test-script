# -*- coding: utf-8 -*-

import sys

sys.path.append("../..")

from common.test_input import TestInput


class SystemInternalEvent(object, TestInput):
    def __init__(self):
        super(SystemInternalEvent, self).__init__()
