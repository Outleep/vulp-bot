"""
Utils logic for discord Bot
"""

import discord

from services.ports.base_ports import BaseBotPort
from .exceptions import BotException


class UtilsBot(BaseBotPort):
    """
    Class for utils logic for discord Bot
    """

    def _get_channel(self, chat_id: int) -> discord.abc.Messageable | None:
        """
        Get channel by id

        Args:
            chat_id (int): channel id

        Returns:
            (discord.TextChannel): channel
        
        Notes:
            If channel not found, return custom Exception
        """

        channel = self.client.get_channel(chat_id)
        if not channel:
            raise BotException("Canal não foi encontrado")

        return channel
