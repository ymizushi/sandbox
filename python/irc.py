#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import re
import time
import socket, string
from threading import Thread
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin  = codecs.getreader('utf_8')(sys.stdin)

SERVER = 'ymizushi.info'
PORT = 6667
NICKNAME = 'kongo-bot'
CHANNEL = '#ymizushi'
PASSWORD = 'kongolove'
TEMPLATE_LIST = [u'やる', '来て', 'きて']
CONFIRM_MESSAGE = u'Dailyやるカナー？'
OUTPUT_SENTENCE = u'デイリーステンダップの時間ネー > 各位'
REAL_NAME = u'yuta_mizushima'

class Time:
    @classmethod
    def now_time(cls):
        return cls(int(time.strftime("%H")), int(time.strftime("%M")))

    def __init__(self, hour, minute):
        if not (0 <= hour <= 24 and 0 <= minute <= 60):
            raise Exception('invalidate datetime')
        self.hour
        self.minute

    def add(self, hour=0, minute=0):
        if self.minute + minute >= 60:
            self.hour += 1
            self.minute = self.minute + minute - 60
        else:
            self.minute += minute
        self.hour += hour

    def is_later_than(self, timer):
        if self.hour > timer.hour:
            return True
        if self.minute > timer.minute:
            return True
        return False
    def equal(self, timer):
        return self.hour == timer.hour and self.minute == timer.minute
LIMIT_TIME = Time(14,45)

class TimeThread(Thread):
    def __init__(self, irc):
        super(TimeThread, self).__init__()
        self.irc = irc
    def run(self):
        while True:
            time.sleep(1.0)
            self.execute()
    def execute(self):
        if Time.now_time().equal(LIMIT_TIME):
            self.ircsend_private_message(CONFIRM_MESSAGE)

import unittest
class TestTime(unittest.TestCase):
    def test_add(self):
        timer = Time(1,5)
        timer.add(1,5)
        self.assertEqual(2, timer.hour)
        self.assertEqual(10, timer.minute)

class Irc:
    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._irc_conn()
        self._login(NICKNAME)
        self._join(CHANNEL)

    def _irc_conn(self):
        self.irc.connect((SERVER, PORT))

    def _login(self, nickname, username='user', password=PASSWORD, realname=REAL_NAME, hostname=SERVER, servername=SERVER):
        self.send_data("PASS %s " % (password))
        self.send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
        self.send_data("NICK %s" % (nickname))

    def _join(self, channel):
        self.send_data("JOIN %s" % channel)

    def send_data(self, command):
        self.irc.send(command + '\n')

    def send_private_message(self, message):
        raw_message = "PRIVMSG %s :%s" % (CHANNEL, message)
        encoded_message = raw_message.encode('utf-8')
        self.send_data(encoded_message)


if __name__ == '__main__':
    irc = Irc()
    time_thread = TimeThread(irc)
    time_thread.start()
    while(True):
        buffer = irc.irc.recv(1024)
        msg = string.split(buffer)
        if msg[0] == "PING":
            irc.send_data("PONG %s" % (msg[1]))
        if msg[1] == 'PRIVMSG':
            message = unicode(reduce(lambda x, y : x+' '+y, msg[3:]), 'utf-8')

            count = 0
            for temp in TEMPLATE_LIST:
                if re.search(temp, message):
                    count += 1
            if count >= 1:
                # if LIMIT_TIME <= int(now_time()) <= LIMIT_TIME+600: 
                if True: 
                    irc.send_private_message(OUTPUT_SENTENCE)
            metched = re.search("\d\d\d\d\d\d", message)
            if metched and re.search(NICKNAME, message):
                print message
                irc.send_private_message(u'ﾘｮｳｶｲﾈｰ > ' + metched.group(0))
                global LIMIT_TIME
                LIMIT_TIME= metched.group(0)
