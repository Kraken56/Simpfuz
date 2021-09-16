import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, syfuz):
        self.syfuz = syfuz

        @syfuz.command()
        async def ping(ctx):
          await ctx.send(f':signal_strength: {round(syfuz.latency * 1000)} ms')


def setup(syfuz):
    syfuz.add_cog(ping(syfuz))
