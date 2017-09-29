#!/usr/bin/env python
import aiml
import sys
import os

os.chdir('../data')
bot = aiml.Kernel()
if os.path.isfile('standard.brn'):
    bot.bootstrap(brainFile='standard.brn')
else:
    bot.bootstrap(learnFiles='startup.xml', commands='load aiml b')
    bot.saveBrain('standard.brn')

while True:
    print bot.respond(raw_input('Enter input >'))
