# -*- coding: utf-8 -*-
"""
actual_result.py derives from test_result.py
It defines actual result and bluetooth serials feedback 

"""
import logging
import sys
from time import sleep

sys.path.append("../..")

from common.test_result import TestResult


class PlatformNotSupportedError(Exception):
    pass


class ActualResult(TestResult):
    """
    ActualResult derives from TestResult
    It implements mock result and actual result read from serial of result and bluetooth ports
    It uses a dictionary to store actual results 
    :static variable dist: test result dictionary
    :static variable result_serial_port: result serial port handler
    :static variable bluetooth_serial_port: bluetooth serial port handler
    """
    result_serial_port = None
    bluetooth_serial_port = None
    dist = {}

    def __init__(self, result_serial_port, bluetooth_serial_port, mock_enable=False):
        """
        constructor of ActualResult
        :param result_serial_port: result serial port handler
        :param bluetooth_serial_port: bluetooth serial port handler
        :param mock_enable: True for mock enable, otherwise disable
        """
        super(ActualResult, self).__init__(mock_enable)
        self.result_serial_port = result_serial_port
        self.bluetooth_serial_port = bluetooth_serial_port

    def set_value(self, key, value):
        """
        set dictionary value according to specified key
        :param key: actual result dictionary key
        :param value: actual result dictionary value
        :return: None
        """
        self.dist[key] = value

    def mock_value(self, key, value):
        """
        set dictionary value according to specified key if mock is enabled
        :param key: actual result dictionary key
        :param value: actual result dictionary value
        :return: None
        """
        if self.mock_enable:
            if key == 'BluetoothSerial':
                logging.debug("if key == 'BluetoothSerial':")
                self.bluetooth_serial_port.mock_readline_data(value)
                self.bluetooth_serial_port.mock_waiting_bytes(len(value))
            else:
                self.set_value(key, value)

    def get_value(self, key):
        """
        get dictionary value according to specified key
        :param key:  actual result dictionary key
        :return: actual result dictionary value
        """
        # read test command to serial port
        if key == 'BluetoothSerial':
            self.dist[key] = self._get_bluetooth_value()
        else:
            out_bytes = ''
            # let's wait one second before reading output (let's give device time to answer)
            sleep(0.1)
            out_buffer_bytes = self.result_serial_port.inWaiting()
            while out_buffer_bytes > 0:
                out_bytes = self.result_serial_port.readline()
                if out_bytes != '':
                    logging.info(out_bytes)
                out_buffer_bytes = self.result_serial_port.inWaiting()
            try:
                return_key = out_bytes[0:out_bytes.index('=')]
            except ValueError:
                logging.error("return_key error:" + out_bytes)
            else:
                if key == return_key:
                    value = out_bytes[out_bytes.index('=') + 1:len(out_bytes)]
                    self.dist[key] = value
                else:
                    logging.error('return key error:' + return_key)

        return self.dist[key]

    def _get_bluetooth_value(self):
        """
        get dictionary value value according to bluetooth specified key
        :return: actual result of bluetooth dictionary value
        """
        # read test command to serial port
        out_bytes = ''
        # let's wait one second before reading output (let's give device time to answer)
        sleep(0.1)
        out_buffer_bytes = self.bluetooth_serial_port.inWaiting()
        while out_buffer_bytes > 0:
            out_bytes = self.bluetooth_serial_port.readline()
            if out_bytes != '':
                logging.info(out_bytes)
            out_buffer_bytes = self.bluetooth_serial_port.inWaiting()

        return out_bytes
