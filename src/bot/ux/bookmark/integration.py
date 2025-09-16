"""
Integration interfaces for bookmark and bookmark pages
"""

from bot.ux.utils.cbutton import CButton
from .interfaces import IBookPage, IBookMark


class Page(IBookPage):
    """
    Page of bookmark
    """

    def __init__(self):
        self.buttons = []
        self.text_inputs = []
        self.labels = []
        self.select_fields = []
        self.description = ""

    async def add_button(self, title, style, callback_action):
        self.buttons.append(
            CButton(
                label=title,
                style=style,
                callback_action=callback_action,
            )
        )

    async def add_text_input(self, title):
        self.text_inputs.append(title)

    async def add_label(self, title):
        self.labels.append(title)

    async def add_description(self, description):
        self.description = description


class Bookmark(IBookMark):
    """
    Bookmark handler
    """
