"""
Ports for comunity logic
"""

from abc import ABC, abstractmethod

import discord

from .base_ports import BaseBotPort


class IComunity(BaseBotPort, ABC):
    """
    Ports for comunity
    """

    @abstractmethod
    async def command_help(self) -> discord.Embed | None:
        """
        Command for help discord commands

        Args:
            chat_id (int | None): chat id
        
        Note: If informed chat_id, send the message in the channel
        """

    @abstractmethod
    async def command_complaint(self) -> discord.Embed | None:
        """
        Command for complaint server

        Args:
            chat_id (int | None): chat id

        Note: If informed chat_id, send the message in the channel
        """
