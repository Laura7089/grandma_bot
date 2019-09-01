import os
from collections import Counter

import yaml

from .common import get_command_args

#############
# CONSTANTS #
#############
COMMAND_STRINGS = (
    "grandmarating",
    "grandmalevel",
    "help",
    "commands",
    "unrecognised",
    "count",
)

REPONSES_DIR = "custom-responses"

CMD_PREFIX = "g!"

HELP_MESSAGE = f"""```
Commands:
{CMD_PREFIX}{COMMAND_STRINGS[0]} NAME - get someone's grandma level
{CMD_PREFIX}{COMMAND_STRINGS[1]} NAME - get someone's grandma rating
{CMD_PREFIX}{COMMAND_STRINGS[5]} - get a list of the top 5 contributors to this channel
{CMD_PREFIX}{COMMAND_STRINGS[2]} or {CMD_PREFIX}{COMMAND_STRINGS[3]} - display this help message
```"""

# Grab all the custom responses files
responses_mapping = dict()
if os.path.isdir(REPONSES_DIR):
    for filename in os.listdir(REPONSES_DIR):
        if filename.split(".")[-1] in ("yaml", "yml"):
            with open(
                    os.path.join(REPONSES_DIR, filename),
                    "rt",
            ) as responses_file:
                responses_mapping.update(
                    yaml.load(
                        responses_file.read(),
                        Loader=yaml.SafeLoader,
                    ))

#################
# CMD FUNCTIONS #
#################


async def grandma_rating(incoming_message):
    myStr = get_command_args(incoming_message)
    if myStr == "":
        return f"Who do you want grandma to rate?\nUse `{CMD_PREFIX}{COMMAND_STRINGS[1]} USERNAME` to tell grandma!"

    response = responses_mapping.get(myStr)
    if response is not None:
        return response[0]

    # Get the last digit of the hash & add 1
    digit = int(str(hash(myStr))[-1]) + 1
    return f"Grandma rates {myStr} **{str(digit)}/10**!"


async def grandma_level(incoming_message):
    myStr = get_command_args(incoming_message)
    if myStr == "":
        return f"Whose grandma level do you want?\nUse `{CMD_PREFIX}{COMMAND_STRINGS[0]} USERNAME` to tell grandma!"

    response = responses_mapping.get(myStr)
    if response is not None:
        return response[1]

    # Get the penultilmate 3 digits from the hash
    level = str(hash(myStr))[-4:-1]
    return f"{myStr}'s grandma level: **{level}**!"


async def get_help(dummy):
    return HELP_MESSAGE


async def get_unrecognised(dummy):
    return f"Grandma doesn't know what you're talking about, try `{CMD_PREFIX}{COMMAND_STRINGS[2]}` for some life lessons!"


async def count_messages(incoming_message):
    MAX_CONTRIBUTORS = 5
    MAX_HISTORY = 500
    messages_list = await incoming_message.channel.history(limit=MAX_HISTORY
                                                           ).flatten()
    contributors = Counter([
        channel_message.author for channel_message in messages_list
    ]).most_common(MAX_CONTRIBUTORS)
    message_formatter = "{0[0].name}#{0[0].discriminator}: {0[1]}"
    top_authors = "\n".join([
        message_formatter.format(element) for element in contributors
        if not element[0].bot
    ])
    return f"""Top {len(contributors)} contributors:
```
{top_authors}
```"""


#########
# LOGIC #
#########
command_map = {
    COMMAND_STRINGS[0]: grandma_rating,
    COMMAND_STRINGS[1]: grandma_level,
    COMMAND_STRINGS[2]: get_help,
    COMMAND_STRINGS[3]: get_help,
    COMMAND_STRINGS[4]: get_unrecognised,
    COMMAND_STRINGS[5]: count_messages,
}


async def bot_command(incoming_message):
    messageArgs = incoming_message.content[len(CMD_PREFIX):].split(" ")
    try:
        return await command_map[messageArgs[0].lower()](incoming_message)
    except KeyError:
        return command_map["unrecognised"](incoming_message)
