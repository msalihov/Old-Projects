from utility_functions import irc_functions


def run(self, msg, to):
    irc_functions.say(self, '\x01ACTION ' + msg + '\x01', to)