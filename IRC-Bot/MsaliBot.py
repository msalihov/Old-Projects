import time

import Connection
import logger
import config


class MsaliBot:
    running = True
    connect = None

    def __init__(self):
        logger.log('Initializing MsaliBot...')
        self.loadconfig()
        self.connect = Connection.Connection(self)
        self.connect.loop()
        try:
            while self.running:
                time.sleep(.1)
        except KeyboardInterrupt:
            if self.running:
                self.shutdown()


    @staticmethod
    def loadconfig():
        logger.log('Loading configuration...')
        logger.log('Nickname: ' + config.get('nickname'))
        logger.log('Channels: ' + str(config.get('channels')))
        logger.log('Hostname: ' + config.get('host'))
        logger.log('Port: ' + str(config.get('port')))

    def shutdown(self):
        self.running = False
        logger.log('Shutting down MsaliBot...')
        self.connect.interrupt()
        logger.log('Shutdown complete')