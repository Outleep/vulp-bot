"""
Interface for input
"""

from typing import List, Callable, Awaitable

import discord
from discord.ui import TextInput, Modal


class CForm(Modal):
    """
    Custom modal
    """
    def __init__(
        self,
        title: str,
        timeout: float,
        inputs: List[TextInput],
        callback_action: Callable[[discord.Interaction, List[TextInput]], Awaitable[None]],
    ):
        super().__init__(
            title=title,
            timeout=timeout,
        )

        self.callback_action = callback_action
        for iei in inputs:
            self.add_item(iei)

    async def on_submit(self, interaction):   # pylint: disable=arguments-differ
        """
        Custom action callback
        """
        if self.callback_action is None:
            return
        await self.callback_action(interaction, [child for child in self.children])
