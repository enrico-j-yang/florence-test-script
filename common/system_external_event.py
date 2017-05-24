# -*- coding: utf-8 -*-

import logging
import sys
from time import sleep

sys.path.append("../..")

from common.test_input import TestInput


class UnknownResultError(Exception):
    pass


class SystemExternalEvent(TestInput):
    mode = "GPIO"
    period = 0
    speed = 0
    control_board_serial_port = None

    def __init__(self, control_board_serial_port, mock_enable=False):
        super(SystemExternalEvent, self).__init__(mock_enable)
        self.control_board_serial_port = control_board_serial_port

    def send(self, value):
        # write test command to serial port
        self.control_board_serial_port.write(value)

        out_bytes = ''
        # let's wait one second before reading output (let's give device time to answer)
        sleep(0.1)
        out_buffer_bytes = self.control_board_serial_port.inWaiting()
        while out_buffer_bytes > 0:
            out_bytes = self.control_board_serial_port.readline()
            if out_bytes != '':
                logging.info(out_bytes)
            out_buffer_bytes = self.control_board_serial_port.inWaiting()

        logging.debug("out_bytes:" + out_bytes)

        if self.mock_enable:
            if out_bytes == 'Result=OK':
                return True
            elif out_bytes == 'Result=Fail':
                return False
            else:
                raise UnknownResultError
        '''
        if str(out_bytes[0:len(out_bytes) - 2].decode('UTF-8')) == 'Result=OK':
            return True
        elif str(out_bytes[0:len(out_bytes) - 2].decode('UTF-8')) == 'Result=Fail':
            return False
        else:
            raise UnknownResultError
        '''

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
        self.send("RatedVoltage=" + str(volt))
