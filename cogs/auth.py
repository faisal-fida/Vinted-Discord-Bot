import logging

import discord
from discord.ext import commands

logger = logging.getLogger("discord")


class AuthCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vinted_session = None

    @discord.app_commands.command(name="log-in", description="Log in to Vinted")
    async def log_in_command(self, interaction: discord.Interaction, username: str, password: str):
        logger.info(f"Logging in as {username}...")
        await interaction.response.send_message(f"Logged in as {username}", ephemeral=True)

    @discord.app_commands.command(name="log-out", description="Log out from Vinted")
    async def log_out_command(self, interaction: discord.Interaction):
        logger.info("Logging out...")
        await interaction.response.send_message("Logged out", ephemeral=True)


async def setup(bot):
    await bot.add_cog(AuthCog(bot))
