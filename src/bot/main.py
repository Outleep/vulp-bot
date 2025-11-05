"""
Main module for startup bot integrations
"""

import os

import discord
from discord import Object
from discord.ext import commands

from integrations.bot_client import client
from setup import setup
from .deps.security import verify_owner_bot


async def load_cogs():
    """
    Function for load cogs
    """

    for filename in os.listdir("./src/bot/cogs/"):
        if filename.endswith(".py"):
            await client.load_extension(f"bot.cogs.{filename[:-3]}")


@client.command(name="csync")
@verify_owner_bot
async def sync_commands(ctx: commands.Context):
    """
    Command for sync tree bot commands
    """

    guild = Object(id=ctx.guild.id)
    await load_cogs()
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


@client.command(name="cclear", description="Limpa a árvore de comandos do bot")
@verify_owner_bot
async def clear_commands(ctx: commands.Context):
    """
    Comando que limpa todos os slash commands do bot
    """
    # Limpa comandos globais
    client.tree.clear_commands(guild=None)

    # Limpa comandos da guild atual
    guild = discord.Object(id=ctx.guild.id)
    client.tree.clear_commands(guild=guild)

    # Sincroniza remoção
    await client.tree.sync(guild=guild)
    await client.tree.sync()

    embed = discord.Embed(
        title="Aviso",
        color=discord.Color.green(),
        description="Árvore de comandos limpa! (globais e desta guild)"
    )
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    """
    Event for startup bot
    """
    await load_cogs()

async def run_bot():
    """
    Main function for startup bot
    """
    async with client:
        await client.start(setup.BOT_TOKEN)
