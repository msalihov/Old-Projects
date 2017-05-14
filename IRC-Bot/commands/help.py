from utility_functions import irc_functions
import config
import cmdhandler


def run(self, to):
    modifiers = "Available prefixes: "
    commands = "Available commands: "
    modarr = config.get('cmdsymbols')
    cmdarr = cmdhandler.getregcmds()
    for x in range(0, len(cmdarr)):
        commands += cmdarr[x] + " "
    for char in modarr:
        modifiers += char + " "
    irc_functions.say(self, modifiers, to)
    irc_functions.say(self, commands, to)