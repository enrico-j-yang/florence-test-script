# -*- coding: utf-8 -*-
'''
system_internal_event.py derives from test_input.py
It defines system internal event class and methods 

'''
import sys

sys.path.append("../..")

from common.test_input import TestInput


class SystemInternalEvent(TestInput):
    '''
    HumanInput derives from TestInput
    :static variable bluetooth_serial_port: bluetooth serial port handler
    '''
    bluetooth_serial_port = None

    def __init__(self, bluetooth_serial_port, mock_enable=False):
        '''
        constructor of SystemInternalEvent
        :param bluetooth_serial_port: bluetooth serial port handler
        :param mock_enable: True for mock enable, otherwise disable
        '''
        super(SystemInternalEvent, self).__init__(mock_enable)
        self.bluetooth_serial_port = bluetooth_serial_port

    def mock_bluetooth_connected(self):
        '''
        mock bluetooth connected signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('IB')
            self.bluetooth_serial_port.write('MG3')
            self.bluetooth_serial_port.write('MU3')

    def mock_bluetooth_disconnected(self):
        '''
        mock bluetooth disconnected signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('IA')
            self.bluetooth_serial_port.write('MG1')
            self.bluetooth_serial_port.write('MU1')

    def mock_bluetooth_connecting(self):
        '''
        mock bluetooth connecting signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG2')
            self.bluetooth_serial_port.write('MU2')

    def mock_bluetooth_music_information(self, name, author, index='', count=''):
        '''
        mock bluetooth music information signal if mock enable
        :param name: music name
        :param author: music author
        :param index: music index
        :param count: music count
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MI' + name + '\xff' + author + '\xff' + index + '\xff' + count)

    def mock_bluetooth_music_playing(self):
        '''
        mock bluetooth music playing signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MB')

    def mock_bluetooth_music_pause(self):
        '''
        mock bluetooth music pause signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MA')

    def mock_bluetooth_dialing(self, number):
        '''
        mock bluetooth dialing signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG4')
            self.bluetooth_serial_port.write('IC' + number)

    def mock_bluetooth_incoming_call(self, number):
        '''
        mock bluetooth incoming call signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG5')
            self.bluetooth_serial_port.write('ID' + number)

    def mock_bluetooth_calling(self, number):
        '''
        mock bluetooth calling signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG6')
            self.bluetooth_serial_port.write('IR' + number)

    def mock_bluetooth_hangup_call(self):
        '''
        mock bluetooth hang up call signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('MG3')
            self.bluetooth_serial_port.write('IF')

    def mock_bluetooth_launched(self):
        '''
        mock bluetooth launched signal if mock enable
        :return: None
        '''
        if self.mock_enable:
            self.bluetooth_serial_port.write('IS')
