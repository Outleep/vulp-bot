"""
Module contains interfaces for bookmarks handler
"""

from typing import Callable, List, Tuple, Coroutine
from abc import ABC, abstractmethod

import discord


class IBookPage(ABC):
    """
    Page interface handler
    """

    @abstractmethod
    async def add_button(
        self,
        title: str,
        style: discord.enums.ButtonStyle,
        callback_action: Coroutine[None, None, None]
    ) -> None:
        """
        Add button

        Args:
            title (str): button title
            color (discord.Color): button color
            callback_action (Callable[[], None]): callback action
        """

    @abstractmethod
    async def add_text_input(self, title: str) -> None:
        """
        Add text input

        Args:
            title (str): title
        """

    @abstractmethod
    async def add_label(self, title: str) -> None:
        """
        Add label
        
        Args:
            title (str): title
        """

    @abstractmethod
    async def add_description(self, description: str) -> None:
        """
        Add description

        Args:
            description (str): description
        """


class IBookMark(ABC):
    """
    Bookmark interface handler
    """

    @abstractmethod
    async def add_page(self, page: IBookPage) -> None:
        """
        Add bookmark page

        Args:
            page (BookPageInterface): page
        """

    @abstractmethod
    async def next_page(self) -> None:
        """
        Move to the next page
        """

    @abstractmethod
    async def previous_page(self) -> None:
        """
        Move to the previous page
        """

    @abstractmethod
    async def go_to_page(self, index: int) -> None:
        """
        Go to a specific page by index
        """
