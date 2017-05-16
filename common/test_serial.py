# -*- coding: utf-8 -*-

import serial
import logging


class TestSerial(object, serial.Serial):
    def __init__(self):
        super(TestSerial, self).__init__()
        logging.info("TestSerial")
