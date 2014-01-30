#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from irc import Time
class TestTime(unittest.TestCase):
    def test_now(self):
        timer = Time.now()
        self.assertTrue(isinstance(timer.hour, int))
        self.assertTrue(isinstance(timer.minute, int))

    def test_add(self):
        timer = Time(3, 3)
        timer.add(2,2)
        self.assertEqual(timer.hour, 5)
        self.assertEqual(timer.minute, 5)

    def test_is_later_than(self):
        timerFast  = Time(3, 3)
        timerLater = Time(4, 5)
        self.assertTrue(timerLater.is_later_than(timerFast))

        timerFast = Time(4, 5)
        timerLater  = Time(5, 6)
        self.assertTrue(timerLater.is_later_than(timerFast))

    def test_equal(self):
        timer1  = Time(4, 5)
        timer2  = Time(4, 5)
        self.assertTrue(timer1.equal(timer2))

if __name__ == '__main__':
    unittest.main()
