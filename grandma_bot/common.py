import string


def getText(message):
    try:
        formattedString = message.content[message.content.index(" ") + 1:]
    except ValueError:
        return ""
    return formattedString


def scrubString(myStr):
    return "".join(
        [char for char in myStr.lower() if char in (
            " " + string.ascii_lowercase + string.digits
        )])
