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
    nome: str = Field(default=None, nullable=False)
    descricao: str = Field(default=None, nullable=False)
    data_inicio: datetime = Field(default=None, nullable=False)
    data_fim: datetime = Field(default=None, nullable=False)


class Webhooks(SQLModel, table=True):
    """
    Table for webhooks
    """

    __tablename__ = "webhooks"

    id: int = Field(default=None, primary_key=True)
    url: str = Field(default=None, nullable=False)


class WebhooksMessages(SQLModel, table=True):
    """
    Table for webhooks
    """

    __tablename__ = "webhooks_messages"

    id: int = Field(default=None, primary_key=True)
    webhook_id: int = Field(default=None, nullable=False, foreign_key="webhooks.id")
    message_id: int = Field(default=None, nullable=False)
