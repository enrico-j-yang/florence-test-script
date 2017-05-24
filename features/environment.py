# -*- coding: utf-8 -*-
'''
environment.py is pre-process and post-process for all step implementation files

'''
import logging
import platform
import sys

sys.path.append("../..")

from common.test_input import TestInput
from common.human_input import HumanInput
from common.system_internal_event import SystemInternalEvent
from common.system_external_event import SystemExternalEvent
from common.expected_result import ExpectedResult
from common.actual_result import ActualResult
from common.test_serial import TestSerial

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='florence_test.log',
                    filemode='w')


class PlatformNotSupportedError(Exception):
    pass


def before_all(context):
    '''
    Initial serial ports, test input, test result. Set mock_enable to True to enable mock mode.
    :param context: behave global variable
    :return: None
    '''
    if platform.system() == 'Windows':
        try:
            context.control_board_serial_port = TestSerial(port='COM3',
                                                           baudrate=9600,
                                                           timeout=0,
                                                           parity=TestSerial.PARITY_NONE,
                                                           stopbits=TestSerial.STOPBITS_ONE,
                                                           bytesize=TestSerial.EIGHTBITS,
                                                           mock_enable=True)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

        try:
            context.bluetooth_serial_port = TestSerial(port='COM4',
                                                       baudrate=9600,
                                                       timeout=0,
                                                       parity=TestSerial.PARITY_NONE,
                                                       stopbits=TestSerial.STOPBITS_ONE,
                                                       bytesize=TestSerial.EIGHTBITS,
                                                       mock_enable=True)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

        try:
            context.result_serial_port = TestSerial(port='COM5',
                                                    baudrate=9600,
                                                    timeout=0,
                                                    parity=TestSerial.PARITY_NONE,
                                                    stopbits=TestSerial.STOPBITS_ONE,
                                                    bytesize=TestSerial.EIGHTBITS,
                                                    mock_enable=True)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

    elif platform.system() == 'Darwin':
        try:
            context.control_board_serial_port = TestSerial(port='/dev/tty.wchusbserial14120',
                                                           baudrate=9600,
                                                           timeout=0,
                                                           parity=TestSerial.PARITY_NONE,
                                                           stopbits=TestSerial.STOPBITS_ONE,
                                                           bytesize=TestSerial.EIGHTBITS,
                                                           mock_enable=True)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

        try:
            context.bluetooth_serial_port = TestSerial(port='/dev/tty.wchusbserial14130',
                                                       baudrate=9600,
                                                       timeout=0,
                                                       parity=TestSerial.PARITY_NONE,
                                                       stopbits=TestSerial.STOPBITS_ONE,
                                                       bytesize=TestSerial.EIGHTBITS,
                                                       mock_enable=True)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

        try:
            context.result_serial_port = TestSerial(port='/dev/tty.wchusbserial14140',
                                                    baudrate=9600,
                                                    timeout=0,
                                                    parity=TestSerial.PARITY_NONE,
                                                    stopbits=TestSerial.STOPBITS_ONE,
                                                    bytesize=TestSerial.EIGHTBITS,
                                                    mock_enable=True)
        except TestSerial.SerialException:
            logging.error("TestSerial.SerialException")
            raise TestSerial.SerialException
        except Exception as e:
            logging.error("Unknown exception:" + str(e))
        else:
            logging.info("serial opened")

    else:
        logging.error("platform:" + platform.system() + "not supported")
        raise PlatformNotSupportedError

    context.florenceTestInput = TestInput()
    context.florenceTestInput.sysHIEvt = HumanInput(context.control_board_serial_port, context.bluetooth_serial_port,
                                                    mock_enable=True)
    context.florenceTestInput.sysIntEvt = SystemInternalEvent(context.bluetooth_serial_port, mock_enable=True)
    context.florenceTestInput.sysExtEvt = SystemExternalEvent(context.control_board_serial_port, mock_enable=True)
    context.florenceExpRes = ExpectedResult()
    context.florenceActRes = ActualResult(context.result_serial_port, context.bluetooth_serial_port, mock_enable=True)


def after_all(context):
    '''
    Close all serial port after all feature done
    :param context: behave global variable
    :return: None
    '''
    context.control_board_serial_port.close()
    context.bluetooth_serial_port.close()
    context.result_serial_port.close()


def before_feature(context, feature):
    '''
    Initial control board e-bike mode and rated voltage
    :param context: behave global variable
    :param feature: behave feature name
    :return: None
    '''
    context.florenceTestInput.sysHIEvt.set_mode("GPIO")

    context.florenceTestInput.sysExtEvt.set_rated_voltage(48)
    context.florenceTestInput.sysExtEvt.set_mode("GPIO")

# def after_feature(context, feature):
#    context = context


# def before_scenario(context, scenario):
#    context = context


# def after_scenario(context, scenario):
#    context = context
