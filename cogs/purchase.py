import logging

import discord
from discord.ext import commands
from discord import app_commands

logger = logging.getLogger("discord")


class PurchaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def buy_item(self, item_id):
        logger.info(f"Buying item {item_id}...")

    @app_commands.command(name="buy", description="Purchase an item by ID")
    @app_commands.describe(item_id="The ID of the item to purchase")
    async def buy_command(self, interaction: discord.Interaction, item_id: str):
        """Command to initiate purchase of an item."""
        await self.buy_item(item_id)
        await interaction.response.send_message(
            f"Starting purchase for item {item_id}...", ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(PurchaseCog(bot))
