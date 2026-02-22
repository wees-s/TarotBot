import discord,command,errors
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "tarot!", intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await command.daily(ctx)

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def triad(ctx):
    await command.triad(ctx)

@daily.error
async def daily_error(ctx, error):
    await errors.daily_error(ctx, error)

@triad.error
async def triad_error(ctx, error):
    await errors.triad_error(ctx, error)

client.run("API KEY")