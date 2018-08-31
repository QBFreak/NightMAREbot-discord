import time


class IdleRPGPlayer:
    """
    Input handler to play IdleRPG
    """
    def __init__(self, cmd_prefix):
        self.name = "IdleRPG Player"
        self.cmd_prefix = str(cmd_prefix)
        self.waiting_for_input = False
        self.pause_until = time.time() - 1
        print("Added handler {0} with command cmd_prefix '{1}'".format(self.name, self.cmd_prefix))

    def handle(self, message):
        # If we weren't expecting input, pause for a minute to allow other
        #  players to play the game, we don't want to get confused by messages
        #  intended for them
        if not self.waiting_for_input:
            self.pause_until = time.time() + 60
        # If we're paused, ignore input, it's not for us
        if self.pause_until >= time.time():
            return None
        return None
