import config
from utility_functions import string_functions


def has(sender):
    withperms = config.get('allowed')
    for p in withperms:
        senderinfo = string_functions.getsenderarr(sender)
        allowedinfo = p.split('@')
        if senderinfo['nickname'] == allowedinfo[0] and senderinfo['hostname'] == allowedinfo[1]:
            return True
    return False