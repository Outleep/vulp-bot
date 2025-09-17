# pylint: disable=invalid-name, too-few-public-methods, too-many-instance-attributes

"""
Module for import setup
"""

import os
from typing import TypeVar, Type, AsyncGenerator
from contextlib import asynccontextmanager

from dotenv import dotenv_values
from loguru import logger

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy import create_engine
from database.tables import *  # pylint: disable=unused-wildcard-import


T = TypeVar("T")

class Setup:
    """
    Class contains the environment variables
    and database connection
    """

    def __init__(self):
        """
        Attrs:
            API_PORT : porta da api
            API_NAME: nome da api
            API_HOST: host da api
            API_DESCRIPTION: descricao da api
        """

        self.engine = None
        self.env = dotenv_values(".env")

        # Configurações do BOT
        self.BOT_TOKEN = self.get_env("BOT_TOKEN", type_value=str)
        self.BOT_OWNER_ID = self.get_env("BOT_OWNER_ID", type_value=int)
        self.BOT_LOG_CHAT_ID = self.get_env("BOT_LOG_CHAT_ID", type_value=int)
        self.BOT_GUILD_ID = self.get_env("BOT_GUILD_ID", type_value=int)

    def create_database_file(self):
        """
        Create the database file
        """

        if not os.path.exists("resources/vulp.db"):
            with open("resources/vulp.db", "w", encoding="utf-8"):
                pass

    def create_db_engine(self) -> AsyncEngine:
        """
        Create SQLAlchemy engine
        """
        if self.engine is not None:
            return self.engine

        self.create_database_file()  # Create the database file
        self.engine = create_async_engine("sqlite+aiosqlite:///resources/vulp.db")
        sync_engine = create_engine("sqlite:///resources/vulp.db")
        SQLModel.metadata.create_all(sync_engine)

        return self.engine

    @asynccontextmanager
    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Get async session
        """

        engine = self.create_db_engine()
        async_session = AsyncSession(
            engine,
            expire_on_commit=False,
            autoflush=True
        )

        try:
            yield async_session

        except Exception as err:
            await async_session.rollback()
            raise err

        else:
            await async_session.commit()

        finally:
            await async_session.close()

    def get_env(
        self,
        value: str,
        default_value: str = None,
        type_value: Type[T] = str,
    ) -> T:
        """
        Get the value of the environment variable
        
        Args:
            value: The name of the environment variable
            default_value: The default value to use if the environment variable is not set
            type_value (Type): The type of the environment variable
        
        Returns:
            (TypeVar): The value of the environment variable
    
        Raises:
            ValueError: If the environment variable is not set,
                or if the value is not of the expected type
        """

        try:

            # Try to get the value of the environment variable
            result = self.env.get(value, default_value)
            return type_value(result) if result is not None else default_value

        except ValueError as err:

            # If not getter the value of the environment variable
            # return the default value case not default value
            # raise the error
            if default_value is None:
                raise ValueError(
                    "Variavel de ambiente nao compativel com o tipo "
                    f"esperado: {type_value.__name__}"
                ) from err

            logger.warning(
                "Variavel %s nao encontrada usando o valor padrao: %s",
                value, default_value
            )

            return default_value


setup = Setup()
setup.create_db_engine()
