import socket
import logger
import config


def send(self, message):
    logger.log(message)
    self.socket.send(message + '\r\n')


def isping(data):
    if data.find('PING') != -1:
        return True
    else:
        return False


def ping(self, data):
    if isping(data):
        response = data.split(':')[1]
        send(self, 'PONG :%s' % response)
        if not self.connected:
            perform(self)
            self.connected = True


def say(self, msg, to):
    send(self, 'PRIVMSG %s :%s\r\n' % (to, msg))


def perform(self):
    say(self, 'Logged in on ' + socket.gethostname(), 'msalihov')
    send(self, 'MODE %s +x\r\n' % config.get('nickname'))
    for chan in config.get('channels'):
        send(self, 'JOIN %s +x\r\n' % chan)