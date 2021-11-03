import discord
from discord.ext import commands

with open('token.txt', 'r') as fp:
    TOKEN = fp.read().rstrip()

bot = commands.Bot(command_prefix="pog/")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)