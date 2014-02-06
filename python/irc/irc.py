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
CONFIRM_MESSAGE = u'Dailyやるｶﾅｰ？ > EE shiba Aban ymizushi'
OUTPUT_SENTENCE = u'ﾃﾞｲﾘ-ｽﾃﾝﾀﾞｯﾌﾟの時間ﾈー > 各位'
REAL_NAME = u'yuta_mizushima'

global MESSAGE_MAP
MESSAGE_MAP = [ (u'exit' ,u'ｵﾂｶﾚﾈｰ'), ]

END_COMMAND = [u'おやすみ']
END_MESSAGE = u'See you againﾈ......'

START_MESSAGE = u'ｼｬｷｰﾝ'

class Time:
    @classmethod
    def now(cls):
        return cls(int(time.strftime("%H")), int(time.strftime("%M")), int(time.strftime("%S")))

    def __init__(self, hour, minute, second=0):
        if not (0 <= hour <= 24 and 0 <= minute <= 60):
            raise Exception('invalidate datetime')
        self.hour = hour
        self.minute = minute
        self.second = second

    def add(self, hour=0, minute=0, second=0):
        if self.second + second >= 60:
            self.minute += 1
            self.second += second - 60
        else:
            self.second += second
        if self.minute + minute >= 60:
            self.hour += 1
            self.minute += minute - 60
        else:
            self.minute += minute
        self.hour += hour

    def is_later_than(self, timer):
        if self.hour > timer.hour:
            return True
        if self.minute > timer.minute:
            return True
        if self.second > timer.second:
            return True
        return False
    def equal(self, timer):
        return self.hour == timer.hour and self.minute == timer.minute and self.second == timer.second

global DAILY_TIME
DAILY_TIME = Time(14,45)

class TimeThread(Thread):
    def __init__(self, irc):
        super(TimeThread, self).__init__()
        self.irc = irc
    def run(self):
        while True:
            time.sleep(1.0)
            self.execute()
    def execute(self):
        if Time.now().equal(DAILY_TIME):
            self.irc.send_private_message(CONFIRM_MESSAGE)

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
    time_thread.setDaemon(True)
    time_thread.start()
    irc.send_private_message(START_MESSAGE)
    while(True):
        buffer = irc.irc.recv(1024)
        msg = string.split(buffer)
        if msg[0] == "PING":
            if len(msg) > 1:
                irc.send_data("PONG %s" % (msg[1]))
            else:
                irc.send_data("PONG")
        if msg[1] == 'PRIVMSG':
            message = unicode(reduce(lambda x, y : x+' '+y, msg[3:]), 'utf-8')


            for message_tuple in MESSAGE_MAP:
                if re.search(message_tuple[0], message):
                    irc.send_private_message(message_tuple[1])
            for command in END_COMMAND:
                if re.search(command, message) and re.search(NICKNAME, message):
                    irc.send_private_message(END_MESSAGE)
                    sys.exit(u"Programは終了しました")


            matched = re.search(u'やる', message)
            if matched and re.search(NICKNAME, message):
                matched_word = matched.group(0)
                irc.send_private_message(OUTPUT_SENTENCE)

            matched = re.search('\d\d\d\d', message)
            if matched and re.search(NICKNAME, message):
                matched_word = matched.group(0)
                irc.send_private_message(u'ﾘｮｳｶｲﾈｰ > ' + matched_word)
                DAILY_TIME= Time(int(matched_word[0:2]), int(matched_word[2:4]))

            # limit_time = copy.deepcopy(DAILY_TIME)
            # limit_time.add(0,10)
            # now_time = Time.now()
            # if now_time.is_later_than(DAILY_TIME) and limit_time.is_later_than(now_time): 
            #     irc.send_private_message(OUTPUT_SENTENCE)
