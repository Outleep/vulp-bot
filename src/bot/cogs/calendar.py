"""
Cog for update community calendar
"""

from datetime import datetime

import aiohttp

import discord
from discord import app_commands, Interaction, Object
from discord.ext import commands
from loguru import logger

from setup import setup as settings

from bot.deps.security import has_role
from database.repositories.calendar_repo import CalendarRepo, CalendarTable


class CalendarCog(commands.Cog):
    """
    Help cog handler
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="calendario_adicionar",
        description="Adiciona novo evento no calendario."
    )
    @has_role("Moderadores")
    async def calendar_add(
        self,
        interaction: Interaction,
        titulo: str,
        descricao: str,
        data_inicio: str,
        data_fim: str | None = None,
    ):
        """
        Edit calendar message

        Args:
            interaction (Interaction): interaction
            titulo (str): title
            descricao (str): description
            data_inicio (str): start date (MM-DD HH:MM )
            data_fim (str): end date (MM-DD HH:MM )
        """

        try:

            now_year = datetime.now().year
            start_date_str = f"{now_year}-{data_inicio}:00"

            data_inicio = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
            if data_fim is not None:

                end_date_str = f"{now_year}-{data_fim}:00"
                data_fim = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")

        except ValueError:
            await interaction.response.send_message(
                "Formato de data inválido. Use `MM-DD HH:MM`, exemplo: `09-25 19:00`.",
                ephemeral=True
            )
            return

        async with settings.get_async_session() as session:

            # Open repository
            repo = CalendarRepo(session)

            # Case event already exists
            if await repo.get_by_title(titulo.lower()):
                await interaction.response.send_message(
                    "Ja existe um evento com esse titulo.",
                    ephemeral=True,
                )

                return

            # Create event
            event = CalendarTable(
                titulo=titulo.lower(),
                descricao=descricao,
                data_inicio=data_inicio,
                data_fim=data_fim,
            )

            await repo.create(event)
            await interaction.response.send_message(
                "Evento adicionado com sucesso.", ephemeral=True
            )

            # Flush webhook message
            all_events = await repo.get_all()

            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(
                    settings.COMMUNITY_CALENDAR_WEBHOOK_URL,
                    session=session,
                )

                message_content = ""
                for event in all_events:
                    end_date = event.data_fim.strftime("%d/%m/%Y, %H:%M") if event.data_fim else "Indefinido"
                    message_content += f"**{event.titulo.capitalize()}**\n{event.descricao}\n"
                    message_content += f"📅 {event.data_inicio.strftime("%d/%m/%Y %H:%M")} - " + end_date
                    message_content += "\n\n"

                embed = discord.Embed(
                    title="Calendário",
                    description=message_content,
                    color=discord.Color.dark_gray(),
                )

                embed.set_footer(
                    text=f"Editado por {interaction.user.name}",
                    icon_url=interaction.user.display_avatar.url,
                )

                await webhook.edit_message(
                    settings.COMMUNITY_CALENDAR_WEBHOOK_MESSAGE_ID,
                    embed=embed,
                )

            return

async def setup(bot: commands.Bot):
    """
    Hook for load cog
    """
    await bot.add_cog(CalendarCog(bot), guild=Object(id=settings.BOT_GUILD_ID))
    logger.info("✅ CalendarCog carregado com sucesso")
