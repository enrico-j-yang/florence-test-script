# -*- coding: utf-8 -*-

class TestResult:
    dist = {}

    def __init__(self):
        print "TestResult"

    def set_value(self, key, value):
        self.dist[key] = value

    def mock_value(self, key, value):
        self.set_value(key, value)

    def get_value(self, key):
        return self.dist[key]
