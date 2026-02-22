from discord.ext import commands

async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining = int(error.retry_after)

        hours = remaining // 3600
        minutes = (remaining % 3600) // 60

        await ctx.send(
            f"⏳ Sua carta diária já foi lançada hoje.\n"
            f"Tente novamente em **{hours}h {minutes}min**."
        )

async def triad_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining = int(error.retry_after)

        hours = remaining // 3600
        minutes = (remaining % 3600) // 60

        await ctx.send(
            f"⏳ Sua triade diária já foi lida hoje.\n"
            f"Tente novamente em **{hours}h {minutes}min**."
        )