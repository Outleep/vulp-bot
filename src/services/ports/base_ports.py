"""
Module contains base ports
"""

from functools import wraps
from inspect import iscoroutinefunction
from abc import ABC
import traceback

from loguru import logger

import discord
from discord.ext.commands import Bot

from services.utils.exceptions import BotException
from services.utils.bot_utils import UtilsBot
from setup import setup


class BaseBotPort(UtilsBot, ABC):
    """
    Ports for comunity
    """

    def __init__(self, client: Bot):
        self.client = client

    def __getattribute__(self, name):
        """
        Middleware handler erros
        """
        attr = object.__getattribute__(self, name)
        if callable(attr) and iscoroutinefunction(attr):

            @wraps(attr)
            async def wrapper(*args, **kwargs):
                """
                Wrapper for handle errors
                """
                try:
                    return await attr(*args, **kwargs)

                except BotException as err:
                    logger.warning("Comando invalido foi encontrado: " + err.reason)

                    if err.chat_id or setup.BOT_LOG_CHAT_ID:
                        channel = self.client.get_channel(err.chat_id)
                        channel = channel if channel else self.client.get_channel(setup.BOT_LOG_CHAT_ID)

                        embed = discord.Embed(
                            color=discord.Color.yellow(),
                            description="Motivo: " + err.reason,
                            title="Comando invalido",
                        )

                        await channel.send(embed=embed)

                except Exception as err:  # pylint: disable=broad-exception-caught
                    print("exec")
                    logger.error(
                        "Falha ao executar comando: " + str(err),
                        traceback=traceback.format_exc(),
                    )

                    if setup.BOT_LOG_CHAT_ID:
                        channel = self.client.get_channel(setup.BOT_LOG_CHAT_ID)

                        embed = discord.Embed(
                            color=discord.Color.red(),
                            description=f"Motivo: {err} \n Traceback: {traceback.format_exc()}",
                            title="Falha ao executar comando",
                        )

                        await channel.send(embed=embed)

            return wrapper

        return attr
