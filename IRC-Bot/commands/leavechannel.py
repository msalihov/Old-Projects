from utility_functions import irc_functions


def run(self, target):
    irc_functions.send(self, 'PART %s\r\n' % target)