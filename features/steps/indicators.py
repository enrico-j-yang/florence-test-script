# -*- coding: utf-8 -*-
'''
indicators.py is step implementation file for indicators.feature

'''
import logging
from time import sleep


@when(u'电动车有远光灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Beam=High')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上显示远光灯图标')
def step_impl(context):
    context.florenceExpRes.set_value('Beam', 'High')
    context.florenceActRes.mock_value('Beam', 'High')
    context.florenceActRes.get_value('Beam')
    logging.debug("context.florenceExpRes.Beam: " + str(context.florenceExpRes.dist['Beam']))
    logging.debug("context.florenceActRes.Beam: " + str(context.florenceActRes.dist['Beam']))
    assert context.florenceActRes.dist['Beam'] == context.florenceExpRes.dist['Beam']


@when(u'电动车有近光灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Beam=Low')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上显示近光灯图标')
def step_impl(context):
    context.florenceExpRes.set_value('Beam', 'Low')
    context.florenceActRes.mock_value('Beam', 'Low')
    context.florenceActRes.get_value('Beam')
    logging.debug("context.florenceExpRes.Beam: " + str(context.florenceExpRes.dist['Beam']))
    logging.debug("context.florenceActRes.Beam: " + str(context.florenceActRes.dist['Beam']))
    assert context.florenceActRes.dist['Beam'] == context.florenceExpRes.dist['Beam']


@when(u'电动车没有远近光灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Beam=None')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上不显示远近光灯图标')
def step_impl(context):
    context.florenceExpRes.set_value('Beam', 'None')
    context.florenceActRes.mock_value('Beam', 'None')
    context.florenceActRes.get_value('Beam')
    logging.debug("context.florenceExpRes.Beam: " + str(context.florenceExpRes.dist['Beam']))
    logging.debug("context.florenceActRes.Beam: " + str(context.florenceActRes.dist['Beam']))
    assert context.florenceActRes.dist['Beam'] == context.florenceExpRes.dist['Beam']


@when(u'电动车有左转灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('TurnSignalLamp=Left')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上显示左转灯图标')
def step_impl(context):
    context.florenceExpRes.set_value('TurnSignalLamp', 'Left')
    context.florenceActRes.mock_value('TurnSignalLamp', 'Left')
    context.florenceActRes.get_value('TurnSignalLamp')
    logging.debug("context.florenceExpRes.TurnSignalLamp: " + str(context.florenceExpRes.dist['TurnSignalLamp']))
    logging.debug("context.florenceActRes.TurnSignalLamp: " + str(context.florenceActRes.dist['TurnSignalLamp']))
    assert context.florenceActRes.dist['TurnSignalLamp'] == context.florenceExpRes.dist['TurnSignalLamp']


@when(u'电动车有右转灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('TurnSignalLamp=Right')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上显示右转灯图标')
def step_impl(context):
    context.florenceExpRes.set_value('TurnSignalLamp', 'Right')
    context.florenceActRes.mock_value('TurnSignalLamp', 'Right')
    context.florenceActRes.get_value('TurnSignalLamp')
    logging.debug("context.florenceExpRes.TurnSignalLamp: " + str(context.florenceExpRes.dist['TurnSignalLamp']))
    logging.debug("context.florenceActRes.TurnSignalLamp: " + str(context.florenceActRes.dist['TurnSignalLamp']))
    assert context.florenceActRes.dist['TurnSignalLamp'] == context.florenceExpRes.dist['TurnSignalLamp']


@given(u'面板上有远光灯图标')
def step_impl(context):
    context.florenceActRes.set_value('Beam=', 'High')


@when(u'电动车没有左转灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('TurnSignalLamp=None')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@given(u'面板上有蓝牙图标')
def step_impl(context):
    context.florenceActRes.set_value('Bluetooth=', 'Connected')


@when(u'电动车没有右转灯信号')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('TurnSignalLamp=None')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上显示蓝牙图标')
def step_impl(context):
    context.florenceExpRes.set_value('Bluetooth', 'Connected')
    context.florenceActRes.mock_value('Bluetooth', 'Connected')
    context.florenceActRes.get_value('Bluetooth')
    logging.debug("context.florenceExpRes.Bluetooth: " + str(context.florenceExpRes.dist['Bluetooth']))
    logging.debug("context.florenceActRes.Bluetooth: " + str(context.florenceActRes.dist['Bluetooth']))
    assert context.florenceActRes.dist['Bluetooth'] == context.florenceExpRes.dist['Bluetooth']


@when(u'电动车有{malfunction}故障信号')
def step_impl(context, malfunction):
    if malfunction == 'D6':
        context.florenceTestInput.sysExtEvt.send('HallMalfunction=On')
    elif malfunction == 'D5':
        context.florenceTestInput.sysExtEvt.send('GripShiftMalfunction=On')
    elif malfunction == 'D4':
        context.florenceTestInput.sysExtEvt.send('ControllerMalfunction=On')
    elif malfunction == 'D0':
        context.florenceTestInput.sysExtEvt.send('OpenPhaseMalfunction=On')
    else:
        logging.error("Unknown malfunction code")
        assert 0

    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_generate_signal()


@then(u'面板上显示{malfunction}图标')
def step_impl(context, malfunction):
    if malfunction == u'霍尔故障':
        context.florenceExpRes.set_value('HallMalfunction', 'On')
        context.florenceActRes.mock_value('HallMalfunction', 'On')
        context.florenceActRes.get_value('HallMalfunction')
        logging.debug("context.florenceExpRes.HallMalfunction: " + str(context.florenceExpRes.dist['HallMalfunction']))
        logging.debug("context.florenceActRes.HallMalfunction: " + str(context.florenceActRes.dist['HallMalfunction']))
        assert context.florenceActRes.dist['HallMalfunction'] == context.florenceExpRes.dist['HallMalfunction']
    elif malfunction == u'转把故障':
        context.florenceExpRes.set_value('GripShiftMalfunction', 'On')
        context.florenceActRes.mock_value('GripShiftMalfunction', 'On')
        context.florenceActRes.get_value('GripShiftMalfunction')
        logging.debug(
            "context.florenceExpRes.GripShiftMalfunction: " + str(context.florenceExpRes.dist['GripShiftMalfunction']))
        logging.debug(
            "context.florenceActRes.GripShiftMalfunction: " + str(context.florenceActRes.dist['GripShiftMalfunction']))
        assert context.florenceActRes.dist['GripShiftMalfunction'] == context.florenceExpRes.dist[
            'GripShiftMalfunction']
    elif malfunction == u'控制器故障':
        context.florenceExpRes.set_value('ControllerMalfunction', 'On')
        context.florenceActRes.mock_value('ControllerMalfunction', 'On')
        context.florenceActRes.get_value('ControllerMalfunction')
        logging.debug("context.florenceExpRes.ControllerMalfunction: " + str(
            context.florenceExpRes.dist['ControllerMalfunction']))
        logging.debug("context.florenceActRes.ControllerMalfunction: " + str(
            context.florenceActRes.dist['ControllerMalfunction']))
        assert context.florenceActRes.dist['ControllerMalfunction'] == context.florenceExpRes.dist[
            'ControllerMalfunction']
    elif malfunction == u'电机缺相':
        context.florenceExpRes.set_value('OpenPhaseMalfunction', 'On')
        context.florenceActRes.mock_value('OpenPhaseMalfunction', 'On')
        context.florenceActRes.get_value('OpenPhaseMalfunction')
        logging.debug(
            "context.florenceExpRes.OpenPhaseMalfunction: " + str(context.florenceExpRes.dist['OpenPhaseMalfunction']))
        logging.debug(
            "context.florenceActRes.OpenPhaseMalfunction: " + str(context.florenceActRes.dist['OpenPhaseMalfunction']))
        assert context.florenceActRes.dist['OpenPhaseMalfunction'] == context.florenceExpRes.dist[
            'OpenPhaseMalfunction']
    else:
        logging.error("Unknown malfunction code")
        assert 0


@then(u'面板上{duration}秒后显示{malfunction}图标')
def step_impl(context, duration, malfunction):
    sleep(float(duration))

    if malfunction == u'霍尔故障':
        context.florenceExpRes.set_value('HallMalfunction', 'On')
        context.florenceActRes.mock_value('HallMalfunction', 'On')
        context.florenceActRes.get_value('HallMalfunction')
        logging.debug("context.florenceExpRes.HallMalfunction: " + str(context.florenceExpRes.dist['HallMalfunction']))
        logging.debug("context.florenceActRes.HallMalfunction: " + str(context.florenceActRes.dist['HallMalfunction']))
        assert context.florenceActRes.dist['HallMalfunction'] == context.florenceExpRes.dist['HallMalfunction']
    elif malfunction == u'转把故障':
        context.florenceExpRes.set_value('GripShiftMalfunction', 'On')
        context.florenceActRes.mock_value('GripShiftMalfunction', 'On')
        context.florenceActRes.get_value('GripShiftMalfunction')
        logging.debug(
            "context.florenceExpRes.GripShiftMalfunction: " + str(context.florenceExpRes.dist['GripShiftMalfunction']))
        logging.debug(
            "context.florenceActRes.GripShiftMalfunction: " + str(context.florenceActRes.dist['GripShiftMalfunction']))
        assert context.florenceActRes.dist['GripShiftMalfunction'] == context.florenceExpRes.dist[
            'GripShiftMalfunction']
    elif malfunction == u'控制器故障':
        context.florenceExpRes.set_value('ControllerMalfunction', 'On')
        context.florenceActRes.mock_value('ControllerMalfunction', 'On')
        context.florenceActRes.get_value('ControllerMalfunction')
        logging.debug("context.florenceExpRes.ControllerMalfunction: " + str(
            context.florenceExpRes.dist['ControllerMalfunction']))
        logging.debug("context.florenceActRes.ControllerMalfunction: " + str(
            context.florenceActRes.dist['ControllerMalfunction']))
        assert context.florenceActRes.dist['ControllerMalfunction'] == context.florenceExpRes.dist[
            'ControllerMalfunction']
    elif malfunction == u'电机缺相':
        context.florenceExpRes.set_value('OpenPhaseMalfunction', 'On')
        context.florenceActRes.mock_value('OpenPhaseMalfunction', 'On')
        context.florenceActRes.get_value('OpenPhaseMalfunction')
        logging.debug(
            "context.florenceExpRes.OpenPhaseMalfunction: " + str(context.florenceExpRes.dist['OpenPhaseMalfunction']))
        logging.debug(
            "context.florenceActRes.OpenPhaseMalfunction: " + str(context.florenceActRes.dist['OpenPhaseMalfunction']))
        assert context.florenceActRes.dist['OpenPhaseMalfunction'] == context.florenceExpRes.dist[
            'OpenPhaseMalfunction']
    else:
        logging.error("Unknown malfunction code")
        assert 0
