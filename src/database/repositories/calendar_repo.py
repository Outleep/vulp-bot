"""
Calendar repositorie
"""

from database.tables import CalendarTable
from .base_repo import BaseRepo


class CalendarRepo(BaseRepo[CalendarTable]):
    """
    Calendar repositorie
    """
