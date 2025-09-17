"""
Cogs for presence jobs
"""

from random import choice
from datetime import timedelta, datetime

from ClockParts import Cog

import discord

from loguru import logger

from integrations.bot_client import client


class PresenceCog(Cog):
    """
    Presence cogs
    """

    def __init__(self):
        self.last_presence = None
        self.morning_messages = [
            "Bom dia",
            "Que manhã fria",
            "Espero que o dia seja bom",
            "Academia no frio?",
            "Odeio acordar cedo",
        ]

        self.afternoon_messages = [
            "Boa tarde",
            "Que tarde fria",
            "Espero que o dia seja bom",
            "Odeio acordar tarde",
        ]

        self.night_messages = [
            "Boa noite",
            "Que noite fria",
            "Espero que o dia seja bom",
            "Academia de noite? Nao.",
            "Odeio acordar noite.",
        ]

    @Cog.task(schedule=timedelta(seconds=5))
    async def update_presence(self):
        """
        Schedule for update discord presence based in actual time of day
        """

        now_time = datetime.now()

        match now_time.hour:

            case _ if now_time.hour < 12:
                new_presence = choice(self.morning_messages)

            case _ if now_time.hour < 18:
                new_presence = choice(self.afternoon_messages)

            case _ if now_time.hour < 23:
                new_presence = choice(self.night_messages)

            case _:
                new_presence = choice(self.night_messages)

        if self.last_presence is None or (self.last_presence != new_presence):
            logger.info("Atualizando presença para: " + new_presence)
            self.last_presence = new_presence
            await client.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching, name=new_presence
                )
            )
