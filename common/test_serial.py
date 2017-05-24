# -*- coding: utf-8 -*-

import logging

import serial


class MockSerial:
    instance_counter = 0
    waiting_bytes = len("Result=OK")
    readline_data = ("Result=OK" + '\r\n').encode("utf-8")

    def __init__(self):
        logging.debug("MockSerial")
        MockSerial.instance_counter += 1
        self.instance_counter = MockSerial.instance_counter

    def open(self):
        logging.debug("MockSerial open")

    def close(self):
        logging.debug("MockSerial close")

    def read(self, size=1):
        logging.debug("MockSerial read")
        return size

    def write(self, data):
        logging.debug("MockSerial write")
        return len(data)

    def flush(self):
        logging.debug("MockSerial flush")

    def inWaiting(self):
        logging.debug("MockSerial inWaiting")
        if self.waiting_bytes == 0:
            self.waiting_bytes = len("Result=OK")
            return 0
        else:
            self.waiting_bytes = 0
            return len("Result=OK")

    def outWaiting(self):
        logging.debug("MockSerial outWaiting")
        return 0

    def readline(self):
        logging.debug("MockSerial readline")
        return self.readline_data

    @property
    def port(self):
        return 'mock_port' + str(self.instance_counter)

    def mock_waiting_bytes(self, waiting_bytes):
        self.waiting_bytes = waiting_bytes

    def mock_readline_data(self, readline_data):
        self.readline_data = (readline_data + '\r\n').encode("utf-8")


class TestSerial:
    serial_port = None
    mock_enable = True
    # serial byte size
    FIVEBITS = serial.FIVEBITS
    SIXBITS = serial.FIVEBITS
    SEVENBITS = serial.FIVEBITS
    EIGHTBITS = serial.FIVEBITS
    # serial parity
    PARITY_NONE = serial.PARITY_NONE
    PARITY_EVEN = serial.PARITY_EVEN
    PARITY_ODD = serial.PARITY_ODD
    PARITY_MARK = serial.PARITY_MARK
    PARITY_SPACE = serial.PARITY_SPACE
    # serial stopbits
    STOPBITS_ONE = serial.STOPBITS_ONE
    STOPBITS_ONE_POINT_FIVE = serial.STOPBITS_ONE_POINT_FIVE
    STOPBITS_TWO = serial.STOPBITS_TWO

    class SerialException(Exception):
        pass

    def __init__(self,
                 port=None,
                 baudrate=9600,
                 bytesize=EIGHTBITS,
                 parity=PARITY_NONE,
                 stopbits=STOPBITS_ONE,
                 timeout=None,
                 xonxoff=False,
                 rtscts=False,
                 write_timeout=None,
                 dsrdtr=False,
                 inter_byte_timeout=None,
                 exclusive=None,
                 mock_enable=False):
        if mock_enable == True:
            self.mock_enable = mock_enable
            self.serial_port = MockSerial()
        else:
            self.serial_port = serial.Serial()
            self.serial_port.port = port
            self.serial_port.baudrate = baudrate
            self.serial_port.bytesize = bytesize
            self.serial_port.parity = parity
            self.serial_port.stopbits = stopbits
            self.serial_port.timeout = timeout
            self.serial_port.xonxoff = xonxoff
            self.serial_port.rtscts = rtscts
            self.serial_port.write_timeout = write_timeout
            self.serial_port.dsrdtr = dsrdtr
            self.serial_port.inter_byte_timeout = inter_byte_timeout
            self.serial_port.exclusive = exclusive
            self.serial_port.enable = mock_enable

        try:
            self.serial_port.open()
        except Exception as e:
            logging.error("error open serial port: " + str(e))

        logging.info("TestSerial port " + self.serial_port.port + " opened")

    def enable(self):
        self.mock_enable = True

    def disable(self):
        self.mock_enable = False

    def is_enable(self):
        return self.mock_enable

    def close(self):
        self.serial_port.close()

    def read(self, size=1):
        return self.serial_port.read(size)

    def write(self, data):
        logging.info("Serial:" + self.serial_port.port + " Send:" + data)
        return self.serial_port.write((data + '\r\n').encode("utf-8"))

    def flush(self):
        self.serial_port.flush()

    def inWaiting(self):
        return self.serial_port.inWaiting()

    def outWaiting(self):
        return self.serial_port.outWaiting()

    def readline(self):
        data = self.serial_port.readline()
        logging.info("Serial:" + self.serial_port.port + " Read:" + str(data[0:len(data) - 2].decode('utf-8')))
        return str(data[0:len(data) - 2].decode('utf-8'))

    def mock_waiting_bytes(self, waiting_bytes):
        if self.mock_enable:
            self.serial_port.mock_waiting_bytes(waiting_bytes)

    def mock_readline_data(self, readline_data):
        if self.mock_enable:
            self.serial_port.mock_readline_data(readline_data)
