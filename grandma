#!/usr/bin/env python3
import logging

import grandmaBot

# Set up logging
LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.INFO)
handler = logging.FileHandler(filename='lastRun.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
LOGGER.addHandler(handler)

# Initialise a client
client = grandmaBot.grandmaClient()
with open("clientID.txt") as id_file:
    myID = id_file.read()
client.run(myID)
