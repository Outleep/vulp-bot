"""
Cog for help command
"""

from discord import app_commands, Interaction, Object
from discord.ext import commands
from loguru import logger

from setup import setup as settings


class HelpCog(commands.Cog):
    """
    Help cog handler
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ajuda",
        description="Visualizar comandos e informações uteis do servidor."
    )
    async def help(self, interaction: Interaction):
        """
        Send help message
        """

async def setup(bot: commands.Bot):
    """
    Hook for load cog
    """
    await bot.add_cog(HelpCog(bot), guild=Object(id=settings.BOT_GUILD_ID))
    logger.info("✅ HelpCog carregado com sucesso")
