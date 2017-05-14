from utility_functions import irc_functions


def run(self, msg, to):
    irc_functions.say(self, msg, to)