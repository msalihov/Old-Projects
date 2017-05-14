from utility_functions import string_functions
from utility_functions import irc_functions
import config

#Command Imports
from pubcmds import killmsg
from pubcmds import weatherinfo


def iscmd(infoarr):
    for char in config.get('pubcmdsymbols'):
        if infoarr['msg'].startswith(char):
            return True
    return False


def getcmd(infoarr):
    return infoarr['msg'].split(' ')[0].replace('.', '')


def isreg(cmd):
    cmdarr = getregcmds()
    for x in range(0, len(cmdarr)):
        if cmdarr[x] == cmd:
            return True
    return False


def getregcmds():
    cmdarr = config.get('pubcmds')
    ident = 0
    arr = {}
    for cmd in cmdarr:
        arr[ident] = cmd.split(':')[1]
        ident += 1
    return arr


def getmappedaction(cmd):
    cmdarr = config.get('pubcmds')
    for com in cmdarr:
        cmdsp = com.split(':')
        if cmdsp[1] == cmd:
            return cmdsp[0]
    return cmd


def getparam(number, infoarr):
    number += 1
    return infoarr['msg'].split(' ')[number]


def getjoinedparams(start, infoarr):
    start += 1
    string = ""
    messagearr = infoarr['msg'].split(' ')
    for x in range(start, len(messagearr)):
        string += messagearr[x] + " "
    return string


def getparamslength(infoarr):
    messagearr = infoarr['msg'].split(' ')
    return len(messagearr) - 1


def handle(self, infoarr):
    if iscmd(infoarr):
        command = getcmd(infoarr)
        sender = string_functions.getsender(infoarr['sender'])
        if isreg(command):
            action = getmappedaction(command)
            if action == "killmsg":
                if getparamslength(infoarr) >= 1:
                    target = getjoinedparams(0, infoarr)
                    location = infoarr['target']
                    killmsg.run(self, location, target)
            if action == "weatherinfo":
                if getparamslength(infoarr) >= 1:
                    target = infoarr['target']
                    location = getparam(0, infoarr)
                    weatherinfo.run(self, target, location)