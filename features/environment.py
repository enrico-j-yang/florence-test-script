# -*- coding: utf-8 -*-

import sys

sys.path.append("../..")

from common.test_input import TestInput
# from common.human_input import HumanInput
# from common.system_internal_event import SystemInternalEvent
from common.system_external_event import SystemExternalEvent
from common.expected_result import ExpectedResult
from common.actual_result import ActualResult


def before_all(context):
    context.florenceTestInput = TestInput()
    context.florenceTestInput.sysExtEvt = SystemExternalEvent()
    context.florenceExpRes = ExpectedResult()
    context.florenceActRes = ActualResult()


def after_all(context):
    context = context


def before_feature(context, feature):
    context.florenceTestInput.sysExtEvt.set_mode("GPIO")
    context.florenceTestInput.sysExtEvt.set_rated_voltage(48)


def after_feature(context, feature):
    context = context


def before_scenario(context, scenario):
    context = context


def after_scenario(context, scenario):
    context = context
