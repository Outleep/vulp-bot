"""
Calendar service
"""

from abc import ABC, abstractmethod

from .base_ports import BaseBotPort


class ICalendar(BaseBotPort, ABC):
    """
    Ports for comunity
    """

    @abstractmethod
    async def add_event(self, title: str, description: str) -> None:
        """
        Add event to calendar

        Args:
            title (str): event title
            description (str): event description
        """
