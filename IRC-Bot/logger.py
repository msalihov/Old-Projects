import datetime
from utility_functions import string_functions

FILE_NAME = 'log.txt'
MSG_LOG = 'messages.txt'


def log(message):
    print '[' + str(datetime.datetime.now())[:19] + '] ' + message
    logfile = open(FILE_NAME, 'a')
    logfile.write('[' + str(datetime.datetime.now())[:19] + '] ' + message + '\n')
    logfile.close()


def logmsg(message):
    infoarr = string_functions.getdataarray(message)
    logfile = open(MSG_LOG, 'a')
    logfile.write(
        '[' + infoarr['target'] + ' ' + str(datetime.datetime.now())[:19] + '] <' + infoarr['sender'].split('!')[
            0] + '> ' + infoarr['msg'] + '\n')
    logfile.close()