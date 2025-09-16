"""
Integration for the discord bot
"""

import discord
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="vulp!")
