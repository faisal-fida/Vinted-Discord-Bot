from discord.ext import commands
import os

TOKEN = os.getenv('MTMyNTQ5NzMyODA0Nzc1MTE2OQ.GCXuPd.YBbuiD86ISmp2UKE9cjZBnPd0xxI3C58w8l_yU')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)