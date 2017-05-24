# -*- coding: utf-8 -*-
import logging


class TestInput:
    sysExtEvt = None
    sysIntEvt = None
    humanInputEvt = None
    mock_enable = False

    def __init__(self, mock_enable=False):
        self.mock_enable = mock_enable
        if self.mock_enable:
            logging.debug('TestInput enable')
        else:
            logging.debug('TestInput')
