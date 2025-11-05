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
            "O sol nasce, mas algo espreita no silêncio da manhã...",
            "Frio que corta, como se guardasse segredos não ditos.",
            "Que este dia revele mais do que simples horas.",
            "Acordar cedo... ou ser acordado pelo próprio destino?",
            "Há algo estranho no ar desta manhã, você sente?",
        ]

        self.afternoon_messages = [
            "O tempo se arrasta, e a tarde guarda mistérios ocultos.",
            "Frio na tarde... ou apenas um aviso velado?",
            "Que esta tarde não seja comum, mas um presságio.",
            "A tarde desperta sombras que poucos percebem.",
        ]

        self.night_messages = [
            "A noite sussurra segredos que não ousamos repetir.",
            "O frio da noite... ou apenas o mundo segurando a respiração?",
            "Que a escuridão traga respostas — ou mais perguntas.",
            "Alguns lugares não devem ser visitados...",
            "Acordar à noite... mas será que foi você quem acordou?",
        ]

    @Cog.task(schedule=timedelta(minutes=5))
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
