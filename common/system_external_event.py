# -*- coding: utf-8 -*-

import sys

sys.path.append("../..")
import logging

from common.test_input import TestInput


class SystemExternalEvent(object, TestInput):
    ser = None
    mode = "GPIO"
    period = 0
    speed = 0

    def __init__(self):
        super(SystemExternalEvent, self).__init__()

    def send(self, value):
        self.ser = value
        # write test command to serial port
        logging.info("SerialWrite:" + value)

    def set_mode(self, mode):
        self.mode = mode
        self.send("Mode=" + mode)

    def set_signal_period(self, period):
        self.send("SignalPeriod=" + str(period))
        self.period = period

    def start_commit_signal(self):
        self.send("Signal=Start")

    def stop_commit_signal(self):
        self.send("Signal=Stop")

    def set_rated_voltage(self, volt):
        self.send("RatedVoltage="+str(volt))
