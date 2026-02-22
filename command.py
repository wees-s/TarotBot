import discord, os, random
from chat import response_tarot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARDS_DIR = os.path.join(BASE_DIR, "cards")

async def daily(ctx):
    card = random.choice(os.listdir(CARDS_DIR))
    await ctx.send(file=discord.File(f"{CARDS_DIR}/{card}"))
    await ctx.send(response_tarot(f"O que a carta {card} pode significar para minha vida no dia de hoje? | instruções: (resuma em 20 palavras ou menos, responda de forma engraçada)"))

async def triad(ctx):
    cards = random.sample(os.listdir(CARDS_DIR), 3)
    await ctx.send(file=discord.File(f"{CARDS_DIR}/{cards[0]}"))
    await ctx.send(response_tarot(f"O que a carta {cards[0]} pode significar para minha vida? | instruções: (resuma em 20 palavras ou menos, responda de forma engraçada)"))
    await ctx.send(file=discord.File(f"{CARDS_DIR}/{cards[1]}"))
    await ctx.send(response_tarot(f"O que a carta {cards[1]} pode significar para minha vida? | instruções: (resuma em 20 palavras ou menos, responda de forma engraçada)"))
    await ctx.send(file=discord.File(f"{CARDS_DIR}/{cards[2]}"))
    await ctx.send(response_tarot(f"O que a carta {cards[2]} pode significar para minha vida? | instruções: (resuma em 20 palavras ou menos, responda de forma engraçada)"))