#!/usr/bin/env python3
import logging

from grandma_bot import client

# Set up logging
LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='lastRun.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('[%(asctime)s:%(levelname)s:%(name)s]  %(message)s'))
LOGGER.addHandler(handler)
LOGGER.addHandler(logging.StreamHandler())

# Initialise a client
my_client = client.GrandmaClient()
with open("clientID.txt") as id_file:
    myID = id_file.readline().replace("\n", "")
my_client.run(myID)