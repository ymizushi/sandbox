#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import re
import time
import socket, string
from threading import Thread, Event, Lock
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
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LIMIT_TIME = '025400'

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
def login(nickname, username='user', password=PASSWORD, realname=REAL_NAME, hostname=SERVER, servername=SERVER):
    send_data("PASS %s " % (password))
    send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
    send_data("NICK %s" % (nickname))

def now_time():
    return time.strftime("%H%M%S")

def main():
    while(True):
        buffer = IRC.recv(1024)
        print now_time()
        msg = string.split(buffer)
        if msg[0] == "PING":
            print msg
            send_data("PONG %s" % (msg[1]))
        if msg[1] == 'PRIVMSG':
            message = reduce(lambda x,y: x+''+y, msg[3:])
            message = unicode(message,'utf-8')
            count = 0
            for temp in TEMPLATE_LIST:
                if re.search(temp, message):
                    count += 1
            if count >= 1:
                # if LIMIT_TIME <= int(now_time()) <= LIMIT_TIME+600: 
                if True: 
                    send_private_message(OUTPUT_SENTENCE)
            print message
            metched = re.search("\d\d\d\d\d\d", message)
            if metched and re.search(NICKNAME, message):
                print message
                send_private_message(u'ﾘｮｳｶｲﾈｰ > ' + metched.group(0))
                global LIMIT_TIME
                LIMIT_TIME= metched.group(0)

def send_private_message(message):
    raw_message = "PRIVMSG %s :%s" % (CHANNEL, message)
    encoded_message = raw_message.encode('utf-8')
    send_data(encoded_message)

irc_conn()
login(NICKNAME)
join(CHANNEL)

class TimeThread(Thread):
    def run(self):
        while True:
            time.sleep(1.0)
            if now_time() == LIMIT_TIME:
                send_private_message(CONFIRM_MESSAGE)
time_thread = TimeThread()
time_thread.start()

main()

