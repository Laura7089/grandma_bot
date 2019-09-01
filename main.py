#!/usr/bin/env python3
import argparse
import logging
import os

from grandma_bot import client

# Setup arguments
parser = argparse.ArgumentParser(description="Run grandma_bot.")
parser.add_argument(
    "-l",
    "--logfile",
    action="store",
    default="grandma_bot.log",
    help="relative path to the logfile",
)
parser.add_argument(
    "-c",
    "--clientid",
    action="store",
    default=os.environ.get("CLIENT_ID"),
    help="bot's discord account clientID, NOT RECOMMENDED TO PASS VIA THE CLI",
)
parser.add_argument(
    "--loglevel",
    action="store",
    default="info",
    choices=["info", "warning", "debug"],
    help="level of logging to record at",
)

args = parser.parse_args()
log_level = {
    "info": logging.INFO,
    "warning": logging.WARNING,
    "debug": logging.DEBUG,
}[args.loglevel]

# Set up logging
LOGGER = logging.getLogger('discord')
LOGGER.setLevel(log_level)
handler = logging.FileHandler(filename=args.logfile,
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('[%(asctime)s:%(levelname)s:%(name)s]  %(message)s'))
LOGGER.addHandler(handler)
LOGGER.addHandler(logging.StreamHandler())

# Initialise a client
my_client = client.GrandmaClient()
my_client.run(args.clientid)
