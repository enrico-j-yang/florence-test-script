# -*- coding: utf-8 -*-

import logging
from time import sleep


@when(u'电动车有车速信号为{speed}km/h')
def step_impl(context, speed):
    logging.debug("speed: " + speed)
    context.florenceTestInput.sysExtEvt.speed = speed
    context.florenceTestInput.sysExtEvt.send('Speed=' + speed)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示车速为{speed}km/h')
def step_impl(context, speed):
    context.florenceExpRes.set_value('Speed', speed)
    context.florenceActRes.mock_value('Speed', speed)
    context.florenceActRes.get_value('Speed')
    logging.debug("context.florenceExpRes.Speed: " + str(context.florenceExpRes.dist['Speed']))
    logging.debug("context.florenceActRes.Speed: " + str(context.florenceActRes.dist['Speed']))
    assert context.florenceActRes.dist['Speed'] == context.florenceExpRes.dist['Speed']


@when(u'电动车车速在{duration}秒内从{init_speed}km/h增加到{end_speed}km/h')
def step_impl(context, duration, init_speed, end_speed):
    eclipse_time = 0

    logging.debug("eclipse_time:" + str(eclipse_time))
    logging.debug("duration:" + duration)

    # try:
    while eclipse_time < (int(duration) * 1000):
        speed = int(init_speed) + (int(end_speed) - int(init_speed)) * eclipse_time / (int(duration) * 1000)
        logging.debug("speed:" + str(speed))
        context.florenceTestInput.sysExtEvt.send('Speed=' + str(speed))
        context.florenceTestInput.sysExtEvt.set_signal_period(300)
        context.florenceTestInput.sysExtEvt.start_commit_signal()
        sleep(0.3)
        eclipse_time = eclipse_time + 300

        logging.debug("eclipse_time:" + str(eclipse_time))
        # except:
        #    assert 0


@then(u'面板上显示车速在{duration}秒内从{init_speed}km/h增加到{end_speed}km/h')
def step_impl(context, duration, init_speed, end_speed):
    context.florenceExpRes.set_value('Speed', end_speed)
    context.florenceActRes.mock_value('Speed', end_speed)
    context.florenceActRes.get_value('Speed')
    logging.debug("context.florenceExpRes.Speed: " + str(context.florenceExpRes.dist['Speed']))
    logging.debug("context.florenceActRes.Speed: " + str(context.florenceActRes.dist['Speed']))
    assert context.florenceActRes.dist['Speed'] == context.florenceExpRes.dist['Speed']


@when(u'电动车车速在{duration}秒内从{init_speed}km/h减少到{end_speed}km/h')
def step_impl(context, duration, init_speed, end_speed):
    eclipse_time = 0

    logging.debug("eclipse_time:" + str(eclipse_time))
    logging.debug("duration:" + duration)

    # try:
    while eclipse_time < (int(duration) * 1000):
        speed = int(init_speed) + (int(end_speed) - int(init_speed)) * eclipse_time / (int(duration) * 1000)
        context.florenceTestInput.sysExtEvt.send('Speed=' + str(speed))
        context.florenceTestInput.sysExtEvt.set_signal_period(300)
        context.florenceTestInput.sysExtEvt.start_commit_signal()
        sleep(0.3)
        eclipse_time = eclipse_time + 300

        logging.debug("eclipse_time:" + str(eclipse_time))
        # except:
        #    assert 0


@then(u'面板上显示车速在{duration}秒内从{init_speed}km/h减少到{end_speed}km/h')
def step_impl(context, duration, init_speed, end_speed):
    context.florenceExpRes.set_value('Speed', end_speed)
    context.florenceActRes.mock_value('Speed', end_speed)
    context.florenceActRes.get_value('Speed')
    logging.debug("context.florenceExpRes.Speed: " + str(context.florenceExpRes.dist['Speed']))
    logging.debug("context.florenceActRes.Speed: " + str(context.florenceActRes.dist['Speed']))
    assert context.florenceActRes.dist['Speed'] == context.florenceExpRes.dist['Speed']


@then(u'面板上不显示车速')
def step_impl(context):
    context.florenceExpRes.set_value('SpeedVisible', False)
    context.florenceActRes.mock_value('SpeedVisible', False)
    context.florenceActRes.get_value('SpeedVisible')
    logging.debug("context.florenceExpRes.SpeedVisible: " + str(context.florenceExpRes.dist['SpeedVisible']))
    logging.debug("context.florenceActRes.SpeedVisible: " + str(context.florenceActRes.dist['SpeedVisible']))
    assert context.florenceActRes.dist['SpeedVisible'] == context.florenceExpRes.dist['SpeedVisible']


@when(u'电动车有定速设定')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('CruiserMode=On')
    context.florenceTestInput.sysExtEvt.set_signal_period(0)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示定速车速为{speed}km/h')
def step_impl(context, speed):
    context.florenceExpRes.set_value('CruiserMode', 'On')
    context.florenceActRes.mock_value('CruiserMode', 'On')
    context.florenceActRes.get_value('CruiserMode')
    logging.debug("context.florenceExpRes.CruiserMode: " + str(context.florenceExpRes.dist['CruiserMode']))
    logging.debug("context.florenceActRes.CruiserMode: " + str(context.florenceActRes.dist['CruiserMode']))
    assert context.florenceActRes.dist['CruiserMode'] == context.florenceExpRes.dist['CruiserMode']

    context.florenceExpRes.set_value('Speed', speed)
    context.florenceActRes.mock_value('Speed', speed)
    context.florenceActRes.get_value('Speed')
    logging.debug("context.florenceExpRes.Speed: " + str(context.florenceExpRes.dist['Speed']))
    logging.debug("context.florenceActRes.Speed: " + str(context.florenceActRes.dist['Speed']))
    assert context.florenceActRes.dist['Speed'] == context.florenceExpRes.dist['Speed']


@given(u'面板显示的初始总里程为{odo}km')
def step_impl(context, odo):
    context.florenceActRes.set_value('ODO', odo)


@given(u'面板显示的初始单次里程为{trip}km')
def step_impl(context, trip):
    context.florenceActRes.set_value('Trip', trip)


@when(u'电动车车速信号持续{duration}秒')
def step_impl(context, duration):
    eclipse_time = 0

    logging.debug("eclipse_time:" + str(eclipse_time))
    logging.debug("duration:" + duration)

    while eclipse_time < (int(duration) * 1000):
        context.florenceTestInput.sysExtEvt.send('Speed=' + str(context.florenceTestInput.sysExtEvt.speed))
        context.florenceTestInput.sysExtEvt.set_signal_period(300)
        context.florenceTestInput.sysExtEvt.start_commit_signal()
        sleep(0.3)
        eclipse_time = eclipse_time + 300

        logging.debug("eclipse_time:" + str(eclipse_time))


@then(u'面板上显示总里程为{odo}km')
def step_impl(context, odo):
    context.florenceExpRes.set_value('ODO', odo)
    context.florenceActRes.mock_value('ODO', odo)
    context.florenceActRes.get_value('ODO')
    logging.debug("context.florenceExpRes.ODO: " + str(context.florenceExpRes.dist['ODO']))
    logging.debug("context.florenceActRes.ODO: " + str(context.florenceActRes.dist['ODO']))
    assert context.florenceActRes.dist['ODO'] == context.florenceExpRes.dist['ODO']


@then(u'面板上显示单次里程为{trip}km')
def step_impl(context, trip):
    context.florenceExpRes.set_value('Trip', trip)
    context.florenceActRes.mock_value('Trip', trip)
    context.florenceActRes.get_value('Trip')
    logging.debug("context.florenceExpRes.Trip: " + str(context.florenceExpRes.dist['Trip']))
    logging.debug("context.florenceActRes.Trip: " + str(context.florenceActRes.dist['Trip']))
    assert context.florenceActRes.dist['Trip'] == context.florenceExpRes.dist['Trip']


@when(u'用户将电动车熄火')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please shutdown e-bike")


@when(u'用户将电动车打火')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please launch e-bike")


@when(u'电动车有电池电量为{volt_percentage}%')
def step_impl(context, volt_percentage):
    context.florenceTestInput.sysExtEvt.send('Volt=' + volt_percentage)
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示电量为{volt_percentage}%')
def step_impl(context, volt_percentage):
    context.florenceExpRes.set_value('Volt', volt_percentage)
    context.florenceActRes.mock_value('Volt', volt_percentage)
    context.florenceActRes.get_value('Volt')
    logging.debug("context.florenceExpRes.Volt: " + str(context.florenceExpRes.dist['Volt']))
    logging.debug("context.florenceActRes.Volt: " + str(context.florenceActRes.dist['Volt']))
    assert context.florenceActRes.dist['Volt'] == context.florenceExpRes.dist['Volt']


@then(u'面板上显示可持续里程为{available_range}km')
def step_impl(context, available_range):
    context.florenceExpRes.set_value('Range', available_range)
    context.florenceActRes.mock_value('Range', available_range)
    context.florenceActRes.get_value('Range')
    logging.debug("context.florenceExpRes.Range: " + str(context.florenceExpRes.dist['Range']))
    logging.debug("context.florenceActRes.Range: " + str(context.florenceActRes.dist['Range']))
    assert context.florenceActRes.dist['Range'] == context.florenceExpRes.dist['Range']


@then(u'面板上显示可持续里程为{range_in_meter}m')
def step_impl(context, range_in_meter):
    context.florenceExpRes.set_value('Range', range_in_meter * 1000)
    context.florenceActRes.mock_value('Range', range_in_meter * 1000)
    context.florenceActRes.get_value('Range')
    logging.debug("context.florenceExpRes.Range: " + str(context.florenceExpRes.dist['Range']))
    logging.debug("context.florenceActRes.Range: " + str(context.florenceActRes.dist['Range']))
    assert context.florenceActRes.dist['Range'] == context.florenceExpRes.dist['Range']


@when(u'电动车有状态为驻车档')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Status=Park')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示状态为驻车档')
def step_impl(context):
    context.florenceExpRes.set_value('Status', 'Park')
    context.florenceActRes.mock_value('Status', 'Park')
    context.florenceActRes.get_value('Status')
    logging.debug("context.florenceExpRes.Status: " + str(context.florenceExpRes.dist['Status']))
    logging.debug("context.florenceActRes.Status: " + str(context.florenceActRes.dist['Status']))
    assert context.florenceActRes.dist['Status'] == context.florenceExpRes.dist['Status']


@when(u'电动车有状态为可运行')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Status=Ready')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示状态为可运行')
def step_impl(context):
    context.florenceExpRes.set_value('Status', 'Ready')
    context.florenceActRes.mock_value('Status', 'Ready')
    context.florenceActRes.get_value('Status')
    logging.debug("context.florenceExpRes.Status: " + str(context.florenceExpRes.dist['Status']))
    logging.debug("context.florenceActRes.Status: " + str(context.florenceActRes.dist['Status']))
    assert context.florenceActRes.dist['Status'] == context.florenceExpRes.dist['Status']


@when(u'电动车有档位为低速')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Gear=Low')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示档位为低速')
def step_impl(context):
    context.florenceExpRes.set_value('Gear', 'Low')
    context.florenceActRes.mock_value('Gear', 'Low')
    context.florenceActRes.get_value('Gear')
    logging.debug("context.florenceExpRes.Gear: " + str(context.florenceExpRes.dist['Gear']))
    logging.debug("context.florenceActRes.Gear: " + str(context.florenceActRes.dist['Gear']))
    assert context.florenceActRes.dist['Gear'] == context.florenceExpRes.dist['Gear']


@when(u'电动车有档位为中速')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Gear=Medium')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示档位为中速')
def step_impl(context):
    context.florenceExpRes.set_value('Gear', 'Medium')
    context.florenceActRes.mock_value('Gear', 'Medium')
    context.florenceActRes.get_value('Gear')
    logging.debug("context.florenceExpRes.Gear: " + str(context.florenceExpRes.dist['Gear']))
    logging.debug("context.florenceActRes.Gear: " + str(context.florenceActRes.dist['Gear']))
    assert context.florenceActRes.dist['Gear'] == context.florenceExpRes.dist['Gear']


@when(u'电动车有档位为高速')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Gear=High')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上显示档位为高速')
def step_impl(context):
    context.florenceExpRes.set_value('Gear', 'High')
    context.florenceActRes.mock_value('Gear', 'High')
    context.florenceActRes.get_value('Gear')
    logging.debug("context.florenceExpRes.Gear: " + str(context.florenceExpRes.dist['Gear']))
    logging.debug("context.florenceActRes.Gear: " + str(context.florenceActRes.dist['Gear']))
    assert context.florenceActRes.dist['Gear'] == context.florenceExpRes.dist['Gear']


@when(u'电动车有档位为无三速控制')
def step_impl(context):
    context.florenceTestInput.sysExtEvt.send('Gear=None')
    context.florenceTestInput.sysExtEvt.set_signal_period(300)
    context.florenceTestInput.sysExtEvt.start_commit_signal()


@then(u'面板上不显示档位')
def step_impl(context):
    context.florenceExpRes.set_value('Gear', 'None')
    context.florenceActRes.mock_value('Gear', 'None')
    context.florenceActRes.get_value('Gear')
    logging.debug("context.florenceExpRes.Gear: " + str(context.florenceExpRes.dist['Gear']))
    logging.debug("context.florenceActRes.Gear: " + str(context.florenceActRes.dist['Gear']))
    assert context.florenceActRes.dist['Gear'] == context.florenceExpRes.dist['Gear']
