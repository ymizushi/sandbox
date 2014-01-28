#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import re
import time
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin  = codecs.getreader('utf_8')(sys.stdin)
import socket, string

from threading import Thread, Event, Lock


SERVER = 'ymizushi.info'
PORT = 6667
NICKNAME = 'test-bot'
CHANNEL = '#ymizushi'
PASSWORD = 'kongolove'

AND_INPUT_TEMPLATE = [u'やる', '来て', 'きて']

OUTPUT_TEMPLATE = u'デイリースタンドアップの時間です > 各位'

CONFIRM_MESSAGE = u'デイリーやりますですか！？'

#open a socket to handle the connection
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
def irc_conn():
    IRC.connect((SERVER, PORT))

#simple function to send data through the socket
def send_data(command):
    IRC.send(command + '\n')

#join the channel
def join(channel):
    send_data("JOIN %s" % channel)

#send login data (customizable)
def login(nickname, username='user', password=PASSWORD, realname='yuta_mizushima', hostname=SERVER, servername=SERVER):
    send_data("PASS %s " % (password))
    send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
    send_data("NICK " + nickname)

irc_conn()
login(NICKNAME)
join(CHANNEL)


LIMIT_TIME = '042100'

def now_time():
    return time.strftime("%H%M%S")



event = Event()
class TimeThread(Thread):
    def run(self):
        while True:
            time.sleep(1.0)
            if now_time() == LIMIT_TIME:
                confirm_message = "PRIVMSG %s :%s" % (CHANNEL, CONFIRM_MESSAGE)
                encoded_confirm_message = confirm_message.encode('utf-8')
                send_data(encoded_confirm_message)
time_thread = TimeThread()
time_thread.start()


while (1):
    buffer = IRC.recv(1024)
    msg = string.split(buffer)
    if msg[0] == "PING":
        send_data("PONG %s" % msg[1])
    if msg[1] == 'PRIVMSG':
        message = unicode(msg[3],'utf-8')
        count = 0
        for temp in AND_INPUT_TEMPLATE:
            if re.search(temp, message):
                count += 1
        if count >= 1:
            print int(now_time())
            if 40000 <= int(now_time()) <= 160000: 
                output = "PRIVMSG %s :%s" % (CHANNEL, OUTPUT_TEMPLATE)
                hoge = output.encode('utf-8')
                send_data(hoge)
