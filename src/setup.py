# pylint: disable=invalid-name, too-few-public-methods, too-many-instance-attributes

"""
Module for import setup
"""

from typing import TypeVar, Type
from dotenv import dotenv_values
from loguru import logger


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

        self.env = dotenv_values(".env")

        # Configurações do BOT
        self.BOT_TOKEN = self.get_env("BOT_TOKEN", type_value=str)

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
