"""
Calendar repositorie
"""

from sqlalchemy import select

from database.tables import CalendarTable
from .base_repo import BaseRepo


class CalendarRepo(BaseRepo[CalendarTable]):
    """
    Calendar repositorie
    """

    async def get_by_title(self, title: str) -> CalendarTable | None:
        """
        Get calendar by title

        Args:
            title (str): title

        Returns:
            CalendarTable | None: calendar
        """

        stmt = select(self.model).where(self.model.titulo == title)
        result = await self.session.execute(stmt)
        return result.scalars().one_or_none()