from utility_functions import string_functions
from utility_functions import irc_functions
import perms
import config

#Command Imports
from commands import disconnect
from commands import sendprivmsg
from commands import help
from commands import sendaction
from commands import joinchannel
from commands import leavechannel


def iscmd(infoarr):
    for char in config.get('cmdsymbols'):
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
    cmdarr = config.get('commands')
    ident = 0
    arr = {}
    for cmd in cmdarr:
        arr[ident] = cmd.split(':')[1]
        ident += 1
    return arr


def getmappedaction(cmd):
    cmdarr = config.get('commands')
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
            if perms.has(infoarr['sender']):
                if action == 'disconnect':
                    disconnect.run(self.msabot)
                elif action == 'sendprivmsg':
                    if getparamslength(infoarr) >= 2:
                        message = getjoinedparams(1, infoarr)
                        target = getparam(0, infoarr)
                        sendprivmsg.run(self, message, target)
                        irc_functions.say(self, 'Private message sent', sender)
                    else:
                        irc_functions.say(self, 'Not enough arguments for %s' % command, sender)
                elif action == 'help':
                    help.run(self, sender)
                elif action == 'sendaction':
                    if getparamslength(infoarr) >= 2:
                        message = getjoinedparams(1, infoarr)
                        target = getparam(0, infoarr)
                        sendaction.run(self, message, target)
                        irc_functions.say(self, 'Action message sent', sender)
                    else:
                        irc_functions.say(self, 'Not enough arguments for %s' % command, sender)
                elif action == 'joinchannel':
                    if getparamslength(infoarr) >= 1:
                        target = getparam(0, infoarr)
                        joinchannel.run(self, target)
                    else:
                        irc_functions.say(self, 'Not enough arguments for %s' % command, sender)
                elif action == 'leavechannel':
                    if getparamslength(infoarr) >= 1:
                        target = getparam(0, infoarr)
                        leavechannel.run(self, target)
                    else:
                        irc_functions.say(self, 'Not enough arguments for %s' % command, sender)
            else:
                irc_functions.say(self, 'You do not have permission', sender)
        else:
            irc_functions.say(self, 'Command %s does not exist!' % command, sender)