"""
Tables for database
"""

from datetime import datetime

from sqlmodel import Field, SQLModel


class CalendarTable(SQLModel, table=True):
    """
    Table for calendar
    """

    __tablename__ = "calendario"

    id: int = Field(default=None, primary_key=True)
    titulo: str = Field(default=None, nullable=False)
    descricao: str = Field(default=None, nullable=False)
    data_inicio: datetime = Field(default=None, nullable=False)
    data_fim: datetime = Field(default=None, nullable=True)
