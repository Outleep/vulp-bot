"""
Module for adapter comunity Port
"""

import discord

from services.ports import ComunityPort
from services.utils import UtilsBot


class ComunityAdapter(ComunityPort, UtilsBot):
    """
    Adapter for ComunityPort
    """

    async def command_help(self, chat_id: int | None) -> discord.Embed | None:

        embed = discord.Embed(title="Ajuda", color=discord.Color.green())
        embed.description = "Comandos do bot"
        if chat_id:
            channel = self._get_channel(chat_id)
            await channel.send(embed=embed)
            return

        return embed

    async def command_complaint(self, chat_id: int | None) -> discord.Embed | None:

        embed = discord.Embed(title="Reclamar", color=discord.Color.green())
        embed.description = "Reclame aqui"
        if chat_id:
            channel = self._get_channel(chat_id)
            await channel.send(embed=embed)
            return

        return embed
