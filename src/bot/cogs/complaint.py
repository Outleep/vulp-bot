"""
Cog for help command
"""

from discord import app_commands, Interaction, Object
from discord.ext import commands
from loguru import logger

from services.adapters.comunity_adapter import ComunityAdapter
from setup import setup as settings


class ComplaintCog(commands.Cog):
    """
    Complaint cog handler
    """

    def __init__(self, bot):
        self.bot = bot
        self.service = ComunityAdapter(bot)

    @app_commands.command(
        name="denuncia",
        description="Visualizar comandos e informações uteis do servidor."
    )
    async def help(self, interaction: Interaction):
        """
        Send help message
        """
        embed = await self.service.command_complaint(None)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

async def setup(bot: commands.Bot):
    """
    Hook for load cog
    """
    await bot.add_cog(ComplaintCog(bot), guild=Object(id=settings.BOT_GUILD_ID))
    logger.info("✅ ComplaintCog carregado com sucesso")
