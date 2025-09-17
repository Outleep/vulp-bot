"""
Cog for help command
"""

import discord
from discord.ui.text_input import TextInput
from discord import app_commands, Interaction, Object
from discord.ext import commands
from loguru import logger

from bot.ux.utils.cform import CForm
from services.adapters.comunity_adapter import ComunityAdapter
from setup import setup as settings


class ComplaintCog(commands.Cog):
    """
    Complaint cog handler
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.service = ComunityAdapter(bot)

    @app_commands.command(
        name="denuncia",
        description="Visualizar comandos e informações uteis do servidor."
    )
    async def complaint(self, interaction: Interaction):
        """
        Send help message
        """

        # Monta o formulario
        form = CForm(
            title="Denuncia",
            timeout=120,
            inputs=[
                TextInput(
                    label="Motivo",
                    custom_id="Motivo",
                    placeholder="Digite o motivo da denuncia",
                ),
                TextInput(
                    label="Usuario denunciado e/ou grupo de usuarios",
                    placeholder="Digite o id do usuario ou grupo de usuarios",
                    custom_id="Usuario / Grupo de usuarios",
                )
            ],
            callback_action=self.callback,
        )

        await interaction.response.send_modal(form)
        return

    async def callback(self, interaction: Interaction, text_inputs: list[TextInput]):
        """
        Custom action callback
        """

        # Envia mensagem para o chat de denuncias
        embed = discord.Embed(
            title="Nova denuncia",
            color=discord.Color.yellow(),
            description=f"Enviada por {interaction.user.mention}",
        )

        for text_input in text_inputs:
            embed.add_field(name=text_input.custom_id, value=text_input.value, inline=False)

        channel = self.bot.get_channel(settings.BOT_LOG_CHAT_ID)
        await channel.send(embed=embed)
        await interaction.response.send_message("Denuncia enviada com sucesso!", ephemeral=True)

async def setup(bot: commands.Bot):
    """
    Hook for load cog
    """
    await bot.add_cog(ComplaintCog(bot), guild=Object(id=settings.BOT_GUILD_ID))
    logger.info("✅ ComplaintCog carregado com sucesso")
