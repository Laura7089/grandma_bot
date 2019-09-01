import random
import time

import discord

from .commands import CMD_PREFIX, botCommand
from .common import get_command_args


class GrandmaClient(discord.Client):
    async def on_message(self, message):
        # Exclude our own messages
        if message.author == self.user:
            return

        # If it's a command
        if message.content.startswith(CMD_PREFIX):
            returnMsg = await botCommand(message)
            await message.channel.send(returnMsg)
            return

        # If it's not a command
        mesgQueue = list()
        currentDay = time.strftime("%a").lower()
        scrubbedMsg = get_command_args(message.content)

        # 1 in 1000 change to say "Mother knows best" on any message
        if random.randint(0, 1000) == 1:
            mesgQueue.append("Mother knows best.")

        # Respond to bolo prompts
        if "its friday" in scrubbedMsg:
            if currentDay == "fri":
                mesgQueue.append("Grandma {0} Fridays.".format(
                    random.choice([
                        "likes", "loves", "adores", "hates", "despises",
                        "doesn't mind"
                    ])))
            else:
                mesgQueue.append(
                    f"Grandma thinks you might need a calendar for Christmas, {message.author.mention}."
                )

        # Respond to the word "healing"
        if "healing" in scrubbedMsg:
            mesgQueue.append(f"{message.author.mention}, walk it off.")

        # If we have any messages queued up, send them all (with a space in between)
        if len(mesgQueue) != 0:
            await message.channel.send(" ".join(mesgQueue))
        return

    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="her daughter fail"))
