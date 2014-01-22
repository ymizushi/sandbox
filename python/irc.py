import socket, string

#some user data, change as per your taste
SERVER = 'chat.freenode.net'
PORT = 6667
NICKNAME = 'test-bot'
CHANNEL = '#testymizushi'

#open a socket to handle the connection
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
def irc_conn():
    IRC.connect((SERVER, PORT))

#simple function to send data through the socket
def send_data(command):
    print command
    IRC.send(command + '\n')

#join the channel
def join(channel):
    send_data("JOIN %s" % channel)

#send login data (customizable)
def login(nickname, username='user', password = None, realname='Pythonist', hostname=SERVER, servername=SERVER):
    send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
    send_data("NICK " + nickname)

irc_conn()
login(NICKNAME)
join(CHANNEL)

while (1):
    buffer = IRC.recv(1024)
    msg = string.split(buffer)
    print msg
    if msg[0] == "PING": #check if server have sent ping command
        send_data("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg[1] == 'PRIVMSG':
        send_data("PRIVMSG #testymizushi HOGE")
