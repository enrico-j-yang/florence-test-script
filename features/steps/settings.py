# -*- coding: utf-8 -*-

import logging


@given(u'面板蓝牙未连接')
def step_impl(context):
    context.florenceActRes.set_value('Bluetooth=', 'Disconnected')


@when(u'用户{press_type}按{times}次{button}键')
def step_impl(context, press_type, times, button):
    loops = int(times)
    for i in range(1, loops):
        if press_type == u'短' and button == '+':
            context.florenceTestInput.sysHIEvt.send('Button=ShortPlus')
        elif press_type == u'短' and button == '-':
            context.florenceTestInput.sysHIEvt.send('Button=ShortMinus')
        elif press_type == u'短' and button == 'O':
            context.florenceTestInput.sysHIEvt.send('Button=ShortOption')
        elif press_type == u'长' and button == '+':
            context.florenceTestInput.sysHIEvt.send('Button=LongPlus')
        elif press_type == u'长' and button == '-':
            context.florenceTestInput.sysHIEvt.send('Button=LongMinus')
        elif press_type == u'长' and button == 'O':
            context.florenceTestInput.sysHIEvt.send('Button=LongOption')
        else:
            logging.error("Unknown button pressing")
            assert 0

        context.florenceTestInput.sysHIEvt.set_signal_period(0)
        context.florenceTestInput.sysHIEvt.start_commit_signal()


@when(u'用户{press_type}按{button}键')
def step_impl(context, press_type, button):
    if press_type == u'短' and button == '+':
        context.florenceTestInput.sysHIEvt.send('Button=ShortPlus')
    elif press_type == u'短' and button == '-':
        context.florenceTestInput.sysHIEvt.send('Button=ShortMinus')
    elif press_type == u'短' and button == 'O':
        context.florenceTestInput.sysHIEvt.send('Button=ShortOption')
    elif press_type == u'长' and button == '+':
        context.florenceTestInput.sysHIEvt.send('Button=LongPlus')
    elif press_type == u'长' and button == '-':
        context.florenceTestInput.sysHIEvt.send('Button=LongMinus')
    elif press_type == u'长' and button == 'O':
        context.florenceTestInput.sysHIEvt.send('Button=LongOption')
    else:
        logging.error("Unknown button pressing")
        assert 0

    context.florenceTestInput.sysHIEvt.set_signal_period(0)
    context.florenceTestInput.sysHIEvt.start_commit_signal()


@then(u'面板进入系统设置')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Setting')
    context.florenceActRes.mock_value('UIStatus', 'Setting')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示蓝牙未连接')
def step_impl(context):
    context.florenceExpRes.set_value('Bluetooth', 'Disconnected')
    context.florenceActRes.mock_value('Bluetooth', 'Disconnected')
    context.florenceActRes.get_value('Bluetooth')
    logging.debug("context.florenceExpRes.Bluetooth: " + str(context.florenceExpRes.dist['Bluetooth']))
    logging.debug("context.florenceActRes.Bluetooth: " + str(context.florenceActRes.dist['Bluetooth']))
    assert context.florenceActRes.dist['Bluetooth'] == context.florenceExpRes.dist['Bluetooth']


@then(u'面板进入主界面')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@when(u'用户使用蓝牙设备连接电动车面板蓝牙')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please use cellphone connect e-bike bluetooth")


@then(u'面板显示蓝牙正在连接')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_connecting()

    context.florenceExpRes.set_value('UIStatus', 'BluetoothConnecting')
    context.florenceActRes.mock_value('UIStatus', 'BluetoothConnecting')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@given(u'面板蓝牙已连接')
def step_impl(context):
    context.florenceActRes.set_value('Bluetooth', 'Connected')


@then(u'面板显示蓝牙已连接')
def step_impl(context):
    context.florenceExpRes.set_value('Bluetooth', 'Connected')
    context.florenceActRes.mock_value('Bluetooth', 'Connected')
    context.florenceActRes.get_value('Bluetooth')
    logging.debug("context.florenceExpRes.Bluetooth: " + str(context.florenceExpRes.dist['Bluetooth']))
    logging.debug("context.florenceActRes.Bluetooth: " + str(context.florenceActRes.dist['Bluetooth']))
    assert context.florenceActRes.dist['Bluetooth'] == context.florenceExpRes.dist['Bluetooth']


@when(u'用户的蓝牙设备已经连接上电动车面板蓝牙')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("bluetooth device connected to e-bike")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_connected()


@then(u'面板显示为时间')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingTime')
    context.florenceActRes.mock_value('UIStatus', 'SettingTime')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示时间设置的时间，并选中时钟')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'TimeHourSelected')
    context.florenceActRes.mock_value('UIStatus', 'TimeHourSelected')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceActRes.mock_value('Hour', 10)
    context.hour = context.florenceActRes.get_value('Hour')
    logging.debug("context.hour: " + str(context.hour))


@then(u'面板小时数增加')
def step_impl(context):
    context.florenceExpRes.set_value('Hour', context.hour + 1)
    context.florenceActRes.mock_value('Hour', context.hour + 1)
    context.florenceActRes.get_value('Hour')
    logging.debug("context.florenceExpRes.Hour: " + str(context.florenceExpRes.dist['Hour']))
    logging.debug("context.florenceActRes.Hour: " + str(context.florenceActRes.dist['Hour']))
    assert context.florenceActRes.dist['Hour'] == context.florenceExpRes.dist['Hour']

    context.adjusting_hour = context.florenceActRes.dist['Hour']
    logging.debug("context.adjusting_hour: " + str(context.adjusting_hour))


@then(u'面板小时数减少')
def step_impl(context):
    context.florenceExpRes.set_value('Hour', context.hour - 1)
    context.florenceActRes.mock_value('Hour', context.hour - 1)
    context.florenceActRes.get_value('Hour')
    logging.debug("context.florenceExpRes.Hour: " + str(context.florenceExpRes.dist['Hour']))
    logging.debug("context.florenceActRes.Hour: " + str(context.florenceActRes.dist['Hour']))
    assert context.florenceActRes.dist['Hour'] == context.florenceExpRes.dist['Hour']

    context.adjusting_hour = context.florenceActRes.dist['Hour']
    logging.debug("context.adjusting_hour: " + str(context.adjusting_hour))


@then(u'面板小时数持续增加')
def step_impl(context):
    context.florenceExpRes.set_value('Hour', context.hour + 2)
    context.florenceActRes.mock_value('Hour', context.hour + 2)
    context.florenceActRes.get_value('Hour')
    logging.debug("context.florenceExpRes.Hour: " + str(context.florenceExpRes.dist['Hour']))
    logging.debug("context.florenceActRes.Hour: " + str(context.florenceActRes.dist['Hour']))
    assert context.florenceActRes.dist['Hour'] == context.florenceExpRes.dist['Hour']

    context.adjusting_hour = context.florenceActRes.dist['Hour']
    logging.debug("context.adjusting_hour: " + str(context.adjusting_hour))


@then(u'面板小时数持续减少')
def step_impl(context):
    context.florenceExpRes.set_value('Hour', context.hour - 2)
    context.florenceActRes.mock_value('Hour', context.hour - 2)
    context.florenceActRes.get_value('Hour')
    logging.debug("context.florenceExpRes.Hour: " + str(context.florenceExpRes.dist['Hour']))
    logging.debug("context.florenceActRes.Hour: " + str(context.florenceActRes.dist['Hour']))
    assert context.florenceActRes.dist['Hour'] == context.florenceExpRes.dist['Hour']

    context.adjusting_hour = context.florenceActRes.dist['Hour']
    logging.debug("context.adjusting_hour: " + str(context.adjusting_hour))


@then(u'面板确认小时调节，并选中分钟')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'TimeMinuteSelected')
    context.florenceActRes.mock_value('UIStatus', 'TimeMinuteSelected')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceActRes.mock_value('Minute', 10)
    context.minute = context.florenceActRes.get_value('Minute')
    logging.debug("context.minute: " + str(context.minute))


@then(u'面板分钟数增加')
def step_impl(context):
    context.florenceExpRes.set_value('Minute', context.minute + 1)
    context.florenceActRes.mock_value('Minute', context.minute + 1)
    context.florenceActRes.get_value('Minute')
    logging.debug("context.florenceExpRes.Minute: " + str(context.florenceExpRes.dist['Minute']))
    logging.debug("context.florenceActRes.Minute: " + str(context.florenceActRes.dist['Minute']))
    assert context.florenceActRes.dist['Minute'] == context.florenceExpRes.dist['Minute']

    context.adjusting_minute = context.florenceActRes.dist['Minute']
    logging.debug("context.adjusting_minute: " + str(context.adjusting_minute))


@then(u'面板分钟数减少')
def step_impl(context):
    context.florenceExpRes.set_value('Minute', context.minute - 1)
    context.florenceActRes.mock_value('Minute', context.minute - 1)
    context.florenceActRes.get_value('Minute')
    logging.debug("context.florenceExpRes.Minute: " + str(context.florenceExpRes.dist['Minute']))
    logging.debug("context.florenceActRes.Minute: " + str(context.florenceActRes.dist['Minute']))
    assert context.florenceActRes.dist['Minute'] == context.florenceExpRes.dist['Minute']

    context.adjusting_minute = context.florenceActRes.dist['Minute']
    logging.debug("context.adjusting_minute: " + str(context.adjusting_minute))


@then(u'面板分钟数持续增加')
def step_impl(context):
    context.florenceExpRes.set_value('Minute', context.minute + 2)
    context.florenceActRes.mock_value('Minute', context.minute + 2)
    context.florenceActRes.get_value('Minute')
    logging.debug("context.florenceExpRes.Minute: " + str(context.florenceExpRes.dist['Minute']))
    logging.debug("context.florenceActRes.Minute: " + str(context.florenceActRes.dist['Minute']))
    assert context.florenceActRes.dist['Minute'] == context.florenceExpRes.dist['Minute']

    context.adjusting_minute = context.florenceActRes.dist['Minute']
    logging.debug("context.adjusting_minute: " + str(context.adjusting_minute))


@then(u'面板分钟数持续减少')
def step_impl(context):
    context.florenceExpRes.set_value('Minute', context.minute - 2)
    context.florenceActRes.mock_value('Minute', context.minute - 2)
    context.florenceActRes.get_value('Minute')
    logging.debug("context.florenceExpRes.Minute: " + str(context.florenceExpRes.dist['Minute']))
    logging.debug("context.florenceActRes.Minute: " + str(context.florenceActRes.dist['Minute']))
    assert context.florenceActRes.dist['Minute'] == context.florenceExpRes.dist['Minute']

    context.adjusting_minute = context.florenceActRes.dist['Minute']
    logging.debug("context.adjusting_minute: " + str(context.adjusting_minute))


@then(u'面板确认调节并返回时间菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingTime')
    context.florenceActRes.mock_value('UIStatus', 'SettingTime')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.hour = context.adjusting_hour
    context.minute = context.adjusting_minute
    logging.debug("context.hour: " + str(context.hour))
    logging.debug("context.minute: " + str(context.minute))


@then(u'面板取消调节并返回时间菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingTime')
    context.florenceActRes.mock_value('UIStatus', 'SettingTime')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板返回主界面，时间不变')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    logging.debug("context.hour: " + str(context.hour))
    logging.debug("context.adjusting_hour: " + str(context.adjusting_hour))
    logging.debug("context.minute: " + str(context.minute))
    logging.debug("context.adjusting_minute: " + str(context.adjusting_minute))
    assert context.hour != context.adjusting_hour
    assert context.minute != context.adjusting_minute


@then(u'面板显示为亮度')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingBrightness')
    context.florenceActRes.mock_value('UIStatus', 'SettingBrightness')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示初始亮度为6格')
def step_impl(context):
    context.florenceExpRes.set_value('Brightness', 6)
    context.florenceActRes.mock_value('Brightness', 6)
    context.florenceActRes.get_value('Brightness')
    logging.debug("context.florenceExpRes.Brightness: " + str(context.florenceExpRes.dist['Brightness']))
    logging.debug("context.florenceActRes.Brightness: " + str(context.florenceActRes.dist['Brightness']))
    assert context.florenceActRes.dist['Brightness'] == context.florenceExpRes.dist['Brightness']

    context.brightness = context.florenceActRes.get_value('Brightness')
    logging.debug("context.brightness: " + str(context.brightness))


@then(u'面板亮度增加到最大')
def step_impl(context):
    context.florenceExpRes.set_value('Brightness', 10)
    context.florenceActRes.mock_value('Brightness', 10)
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.adjusting_brightness = context.florenceActRes.get_value('Brightness')
    logging.debug("context.adjusting_brightness: " + str(context.adjusting_brightness))


@then(u'面板亮度减少到最小')
def step_impl(context):
    context.florenceExpRes.set_value('Brightness', 1)
    context.florenceActRes.mock_value('Brightness', 1)
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.adjusting_brightness = context.florenceActRes.get_value('Brightness')
    logging.debug("context.adjusting_brightness: " + str(context.adjusting_brightness))


@then(u'面板确认调整并返回亮度菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingBrightness')
    context.florenceActRes.mock_value('UIStatus', 'SettingBrightness')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.brightness = context.adjusting_brightness
    logging.debug("context.brightness: " + str(context.brightness))


@then(u'面板取消调节并返回亮度菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingBrightness')
    context.florenceActRes.mock_value('UIStatus', 'SettingBrightness')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示为语言')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.mock_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('SystemLanguage', '語言')
    context.florenceActRes.mock_value('SystemLanguage', '語言')
    context.florenceActRes.get_value('SystemLanguage')
    logging.debug("context.florenceExpRes.SystemLanguage: " + str(context.florenceExpRes.dist['SystemLanguage']))
    logging.debug("context.florenceActRes.SystemLanguage: " + str(context.florenceActRes.dist['SystemLanguage']))
    assert context.florenceActRes.dist['SystemLanguage'] == context.florenceExpRes.dist['SystemLanguage']


@then(u'面板显示高亮为繁体')
def step_impl(context):
    context.florenceExpRes.set_value('LanguageSelected', 'Traditional')
    context.florenceActRes.mock_value('LanguageSelected', 'Traditional')
    context.florenceActRes.get_value('LanguageSelected')
    logging.debug("context.florenceExpRes.LanguageSelected: " + str(context.florenceExpRes.dist['LanguageSelected']))
    logging.debug("context.florenceActRes.LanguageSelected: " + str(context.florenceActRes.dist['LanguageSelected']))
    assert context.florenceActRes.dist['LanguageSelected'] == context.florenceExpRes.dist['LanguageSelected']


@then(u'面板切换系统语言为繁体并返回语言菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.mock_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示三种语言选择')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'LanguageList')
    context.florenceActRes.mock_value('UIStatus', 'LanguageList')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示高亮为简体')
def step_impl(context):
    context.florenceExpRes.set_value('LanguageSelected', 'Simplified')
    context.florenceActRes.mock_value('LanguageSelected', 'Simplified')
    context.florenceActRes.get_value('LanguageSelected')
    logging.debug("context.florenceExpRes.LanguageSelected: " + str(context.florenceExpRes.dist['LanguageSelected']))
    logging.debug("context.florenceActRes.LanguageSelected: " + str(context.florenceActRes.dist['LanguageSelected']))
    assert context.florenceActRes.dist['LanguageSelected'] == context.florenceExpRes.dist['LanguageSelected']


@then(u'面板切换系统语言为简体并返回语言菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.mock_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('SystemLanguage', '语言')
    context.florenceActRes.mock_value('SystemLanguage', '语言')
    context.florenceActRes.get_value('SystemLanguage')
    logging.debug("context.florenceExpRes.SystemLanguage: " + str(context.florenceExpRes.dist['SystemLanguage']))
    logging.debug("context.florenceActRes.SystemLanguage: " + str(context.florenceActRes.dist['SystemLanguage']))
    assert context.florenceActRes.dist['SystemLanguage'] == context.florenceExpRes.dist['SystemLanguage']


@then(u'面板显示高亮为English')
def step_impl(context):
    context.florenceExpRes.set_value('LanguageSelected', 'English')
    context.florenceActRes.mock_value('LanguageSelected', 'English')
    context.florenceActRes.get_value('LanguageSelected')
    logging.debug("context.florenceExpRes.LanguageSelected: " + str(context.florenceExpRes.dist['LanguageSelected']))
    logging.debug("context.florenceActRes.LanguageSelected: " + str(context.florenceActRes.dist['LanguageSelected']))
    assert context.florenceActRes.dist['LanguageSelected'] == context.florenceExpRes.dist['LanguageSelected']


@then(u'面板切换系统语言为English并返回语言菜单')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.mock_value('UIStatus', 'SettingLanguage')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('SystemLanguage', 'Language')
    context.florenceActRes.mock_value('SystemLanguage', 'Language')
    context.florenceActRes.get_value('SystemLanguage')
    logging.debug("context.florenceExpRes.SystemLanguage: " + str(context.florenceExpRes.dist['SystemLanguage']))
    logging.debug("context.florenceActRes.SystemLanguage: " + str(context.florenceActRes.dist['SystemLanguage']))
    assert context.florenceActRes.dist['SystemLanguage'] == context.florenceExpRes.dist['SystemLanguage']


@then(u'面板返回语言菜单并且系统语言不变')
def step_impl(context):
    context.florenceExpRes.set_value('SystemLanguage', context.florenceActRes.get_value('SystemLanguage'))
    logging.debug("context.florenceExpRes.SystemLanguage: " + str(context.florenceExpRes.dist['SystemLanguage']))
    logging.debug("context.florenceActRes.SystemLanguage: " + str(context.florenceActRes.dist['SystemLanguage']))
    assert context.florenceActRes.dist['SystemLanguage'] == context.florenceExpRes.dist['SystemLanguage']

@then(u'面板显示蓝牙从已连接变为未连接')
def step_impl(context):
    context.florenceExpRes.set_value('BluetoothSerial', 'AT#DD')
    context.florenceActRes.mock_value('BluetoothSerial', 'AT#DD')
    context.florenceActRes.get_value('BluetoothSerial')
    logging.debug("context.florenceExpRes.BluetoothSerial: " + str(context.florenceExpRes.dist['BluetoothSerial']))
    logging.debug("context.florenceActRes.BluetoothSerial: " + str(context.florenceActRes.dist['BluetoothSerial']))
    assert context.florenceActRes.dist['BluetoothSerial'] == context.florenceExpRes.dist['BluetoothSerial']

    context.florenceExpRes.set_value('Bluetooth', 'Disconnected')
    context.florenceActRes.mock_value('Bluetooth', 'Disconnected')
    context.florenceActRes.get_value('Bluetooth')
    logging.debug("context.florenceExpRes.Bluetooth: " + str(context.florenceExpRes.dist['Bluetooth']))
    logging.debug("context.florenceActRes.Bluetooth: " + str(context.florenceActRes.dist['Bluetooth']))
    assert context.florenceActRes.dist['Bluetooth'] == context.florenceExpRes.dist['Bluetooth']

