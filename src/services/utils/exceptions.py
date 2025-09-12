"""
Module for custom execeptions
"""


class BotException(Exception):
    """
    Class for custom execeptions
    """

    def __init__(self, reason: str, chat_id: int | None = None):
        self.reason = reason
        self.chat_id = chat_id
