import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "tarot!", intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def daily(ctx):
    card = random.choice(os.listdir("./cards"))
    await ctx.send(file=discord.File(f"./cards/{card}"))

@client.command()
async def triad(ctx):
    cards = random.sample(os.listdir("./cards"), 3)    
    await ctx.send(file=discord.File(f"./cards/{cards[0]}"))
    await ctx.send(file=discord.File(f"./cards/{cards[1]}"))
    await ctx.send(file=discord.File(f"./cards/{cards[2]}"))

client.run("xxxxx")