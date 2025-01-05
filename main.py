import os
import logging
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

logger = logging.getLogger("discord")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents, help_command=None, description="Vinted bot")


@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user.name} ({bot.user.id})")

    # Load extensions (cogs)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

    # Sync commands with Discord
    try:
        synced = await bot.tree.sync()
        if synced:
            logger.info("Commands synced with Discord")
        else:
            logger.warning("Commands not synced with Discord")
    except Exception as e:
        logger.error(f"Error syncing commands with Discord: {e}")


bot.run(TOKEN)
