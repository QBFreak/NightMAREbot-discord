class NightMAREbot:
    """
    Input handler for basic NightMAREbot functionality
    """
    def __init__(self, cmd_prefix):
        self.name = "NightMAREbot"
        self.cmd_prefix = str(cmd_prefix)
        print("Added handler {0} with command cmd_prefix '{1}'".format(self.name, self.cmd_prefix))

    def handle(self, message):
        if message.content.startswith(self.cmd_prefix + "ping"):
            return "{0} Pong!".format(message.author.mention)
        if message.content.startswith(self.cmd_prefix + "quit"):
            raise NightMAREbotShutdown
        return None


class NightMAREbotShutdown(Exception):
    pass
