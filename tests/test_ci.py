#!/usr/bin/env python
# coding: utf-8


class TestCi(object):
    """测试

    """

    def __init__(self):
        super(TestCi, self).__init__()

    def setUp(self):
        print "set up"

    def teardown(self):
        print "teardown"

    def test_a(self):
        print "test_a"

    def test_b(self):
        print "test_b"
