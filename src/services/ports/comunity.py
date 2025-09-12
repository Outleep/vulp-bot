"""
Ports for comunity logic
"""

from abc import ABC, abstractmethod

import discord
from discord.ext.commands import Bot


class ComunityPort(ABC):
    """
    Ports for comunity
    """

    def __init__(self, client: Bot):
        self.client = client

    @abstractmethod
    async def command_help(self, chat_id: int | None) -> discord.Embed | None:
        """
        Command for help discord commands

        Args:
            chat_id (int | None): chat id
        
        Note: If informed chat_id, send the message in the channel
        """

    @abstractmethod
    async def command_complaint(self, chat_id: int | None) -> discord.Embed | None:
        """
        Command for complaint server

        Args:
            chat_id (int | None): chat id

        Note: If informed chat_id, send the message in the channel
        """
