"""
Module contains custom button
"""

import discord
from discord.ui import Button
from typing import Optional, Callable, Coroutine

class CButton(Button):
    """
    Custom button with callback
    """

    def __init__(
        self,
        style: discord.ButtonStyle,
        label: str,
        callback_action: Optional[Callable[[discord.Interaction], Coroutine]] = None,
        **kwargs
    ):
        super().__init__(style=style, label=label, **kwargs)
        self.callback_action = callback_action

    async def callback(self, interaction: discord.Interaction):
        """
        Custom action callback
        """
        if self.callback_action is None:
            return
        await self.callback_action(interaction)
