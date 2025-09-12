"""
Main module for startup all integrations for de Application
"""

import asyncio

from bot.main import run_bot

if __name__ == "__main__":
    asyncio.run(run_bot())
