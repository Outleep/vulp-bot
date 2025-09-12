"""
Main module for startup bot integrations
"""

import os

import discord
from discord import Object
from discord.ext import commands

from integrations.bot_client import client
from setup import setup


async def load_cogs():
    """
    Function for load cogs
    """

    for filename in os.listdir("./src/bot/cogs/"):
        if filename.endswith(".py"):
            await client.load_extension(f"bot.cogs.{filename[:-3]}")


@client.command(name="csync")
async def sync_commands(ctx: commands.Context):
    """
    Command for sync tree bot commands
    """

    guild = Object(id=ctx.guild.id)
    commands_loaded = await client.tree.sync(guild=guild)

    embed = discord.Embed(
        title="Aviso",
        color=discord.Color.green(),
        description="Comandos sincronizados!"
    )

    for command in commands_loaded:
        embed.add_field(
            name=command.name,
            value=command.description or "Sem descrição",
            inline=False
        )

    await ctx.send(embed=embed)


async def run_bot():
    """
    Main function for startup bot
    """
    async with client:
        await load_cogs()
        await client.start(setup.BOT_TOKEN)
