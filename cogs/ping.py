import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, syfuz):
        self.syfuz = syfuz

        @syfuz.command()
        async def ping(ctx):
            
            embed=discord.Embed()
            embed.set_thumbnail(url="https://raw.githubusercontent.com/Kraken56/Simpfuz/master/assets/processing.gif")
            embed.add_field(name="Ping", value=f"{round(syfuz.latency * 1000)} ms", inline=True)
            await ctx.send(embed=embed)

def setup(syfuz):
    syfuz.add_cog(ping(syfuz))
