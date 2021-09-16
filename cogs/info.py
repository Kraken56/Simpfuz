import discord
from discord.ext import commands
import sys
import os

class info(commands.Cog):
    def __init__(self, syfuz):
        self.syfuz = syfuz

        @syfuz.command(aliases=['i'])
        async def info(ctx):

            embed=discord.Embed(color=0xb80000, inline=False)
            embed.set_thumbnail(url="")
            embed.add_field(name="Info", value="Hi! I'm Simpfuz, a bot (under construction) by @Fushiguro#1715", inline=True)            
            embed.set_footer(text="Syfuz")
            embed.set_image(url='')

            await ctx.send(embed=embed)



def setup(syfuz):
    syfuz.add_cog(info(syfuz))
