import socket
import time

from utility_functions import socket_functions
from utility_functions import string_functions
from utility_functions import irc_functions
import config
import logger
import cmdhandler
import pubcmdhandler


class Connection:
    msabot = None
    connected = False
    running = False
    socket = None

    def __init__(self, bot):
        logger.log('Initializing IRC connection...')
        self.msabot = bot
        self.running = True
        self.socket = socket.socket()
        self.socket.connect((config.get('host'), config.get('port')))
        irc_functions.send(self, 'NICK %s' % config.get('nickname'))
        irc_functions.send(self, 'USER %(nick)s %(nick)s %(nick)s :%(nick)s' % {'nick': config.get('nickname')})

    def interrupt(self):
        logger.log('Terminating IRC connection...')
        self.running = False
        irc_functions.say(self, 'Logged out on ' + socket.gethostname(), 'msalihov')
        irc_functions.send(self, 'QUIT :%s\r\n' % config.get('quitmsg'))
        time.sleep(3)
        self.socket.close()

    def loop(self):
        while self.running:
            databuffer = self.socket.recv(4096)
            datalns = socket_functions.getdatalines(databuffer)
            for line in datalns:
                line = string_functions.datatostring(line)
                if line == '':
                    continue
                logger.log(line)
                irc_functions.ping(self, line)
                args = line.split(None, 3)
                if len(args) != 4:
                    continue
                arr = string_functions.getdataarray(args)
                if arr['type'] == 'PRIVMSG':
                    if arr['target'] == config.get('nickname'):
                        cmdhandler.handle(self, arr)
                    pubcmdhandler.handle(self, arr)
                    logger.logmsg(args)
