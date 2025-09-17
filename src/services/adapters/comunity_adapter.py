"""
Module for adapter comunity Port
"""

import discord

from services.ports import IComunity


class ComunityAdapter(IComunity):
    """
    Adapter for ComunityPort
    """

    async def command_help(self) -> discord.Embed | None:

        embed = discord.Embed(title="Ajuda", color=discord.Color.green())
        embed.description = "Comandos do bot"
        return embed

    async def command_complaint(self) -> discord.Embed | None:

        embed = discord.Embed(title="Mensagem enviada no seu privado", color=discord.Color.yellow())
        embed.description = "Reclame aqui"

        return embed
