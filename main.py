#!/usr/bin/env python3
import argparse
import logging
import os

from grandma_bot import client

# Setup arguments
parser = argparse.ArgumentParser(description="Run grandma_bot.")
parser.add_argument(
    "-l",
    "--log-file",
    action="store",
    default="grandma_bot.log",
    help="relative path to the logfile",
)
parser.add_argument(
    "-c",
    "--client-id",
    action="store",
    default=os.environ.get("CLIENT_ID"),
    help=
    "bot's discord account clientID - not recommended to pass via the CLI!",
)
args = parser.parse_args()

# Set up logging
LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=args["log-file"],
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('[%(asctime)s:%(levelname)s:%(name)s]  %(message)s'))
LOGGER.addHandler(handler)
LOGGER.addHandler(logging.StreamHandler())

# Initialise a client
my_client = client.GrandmaClient()
my_client.run(args["client-id"])
