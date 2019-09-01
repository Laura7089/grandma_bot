import random
import time

import discord

from .commands import CMD_PREFIX, bot_command
from .common import get_command_args


class GrandmaClient(discord.Client):
    async def on_message(self, message):
        # Exclude our own messages
        if message.author == self.user:
            return

        # If it's a command
        if message.content.startswith(CMD_PREFIX):
            returnMsg = await bot_command(message)
            await message.channel.send(returnMsg)
            return

        # If it's not a command
        mesg_queue = list()
        current_day = time.strftime("%a").lower()
        scrubbed_msg = get_command_args(message.content)

        # 1 in 1000 change to say "Mother knows best" on any message
        if random.randint(0, 1000) == 1:
            mesg_queue.append("Mother knows best.")

        # Respond to bolo prompts
        if "its friday" in scrubbed_msg:
            if current_day == "fri":
                mesg_queue.append("Grandma {0} Fridays.".format(
                    random.choice([
                        "likes", "loves", "adores", "hates", "despises",
                        "doesn't mind"
                    ])))
            else:
                mesg_queue.append(
                    f"Grandma thinks you might need a calendar for Christmas, {message.author.mention}."
                )

        # Respond to the word "healing"
        if "healing" in scrubbed_msg:
            mesg_queue.append(f"{message.author.mention}, walk it off.")

        # If we have any messages queued up, send them all (with a space in between)
        if len(mesg_queue) != 0:
            await message.channel.send(" ".join(mesg_queue))
        return

    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="her daughter fail"))
