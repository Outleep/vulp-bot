"""
Main module for startup all integrations for the Application
"""

import anyio

from bot.main import run_bot
from jobs.main import shaft


async def main():
    """
    Main function for startup all integrations
    """
    async with anyio.create_task_group() as tg:
        tg.start_soon(shaft.main)
        tg.start_soon(run_bot)

if __name__ == "__main__":
    anyio.run(main)
