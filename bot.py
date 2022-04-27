import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix='.')

@bot.command()
async def trade(ctx, *signal):
    if signal.webhook_id:
        await ctx.send(signal)
        print(signal)


bot.run(getenv('TOKEN'))