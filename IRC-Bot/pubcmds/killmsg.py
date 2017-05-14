import random
from commands import sendaction


def run(self, location, target):
    message = random.choice(open('data/kill.txt').readlines()).replace('!TARG!', target).strip()
    sendaction.run(self, message, location)