import string


def get_command_args(message):
    try:
        formatted_string = message.content[message.content.index(" ") + 1:]
    except ValueError:
        return ""
    return formatted_string


def scrub_str(my_str):
    return "".join([
        char for char in my_str.lower()
        if char in (" " + string.ascii_lowercase + string.digits)
    ])
