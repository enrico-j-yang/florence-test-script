# -*- coding: utf-8 -*-

import sys

sys.path.append("../..")

from common.test_input import TestInput


class SystemInternalEvent(TestInput):
    bluetooth_serial_port = None

    def __init__(self, bluetooth_serial_port, mock_enable=False):
        super(SystemInternalEvent, self).__init__(mock_enable)
        self.bluetooth_serial_port = bluetooth_serial_port

    def mock_bluetooth_connected(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('IB')
            self.bluetooth_serial_port.write('MG3')
            self.bluetooth_serial_port.write('MU3')

    def mock_bluetooth_disconnected(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('IA')
            self.bluetooth_serial_port.write('MG1')
            self.bluetooth_serial_port.write('MU1')

    def mock_bluetooth_connecting(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG2')
            self.bluetooth_serial_port.write('MU2')

    def mock_bluetooth_music_information(self, name, author, index='', count=''):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MI' + name + '\xff' + author + '\xff' + index + '\xff' + count)

    def mock_bluetooth_music_playing(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MB')

    def mock_bluetooth_music_pause(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MA')

    def mock_bluetooth_dialing(self, number):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG4')
            self.bluetooth_serial_port.write('IC' + number)

    def mock_bluetooth_incoming_call(self, number):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG5')
            self.bluetooth_serial_port.write('ID' + number)

    def mock_bluetooth_calling(self, number):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG6')
            self.bluetooth_serial_port.write('IR' + number)

    def mock_bluetooth_hangup_call(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG3')
            self.bluetooth_serial_port.write('IF')

    def mock_bluetooth_launched(self):
        if self.mock_enable:
            self.bluetooth_serial_port.write('IS')
