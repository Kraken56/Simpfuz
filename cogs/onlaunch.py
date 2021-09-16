import discord
from discord.ext import commands
import sys
import os

class onlaunch(commands.Cog):
    def __init__(self, syfuz):
        self.syfuz = syfuz
        @syfuz.event
        async def on_ready():
            await syfuz.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="VALORANT"), status=discord.Status.dnd)
            print('Logged in as: Simpfuz')
            print('---------------------')
            print('Simpfuz   is   online')



def setup(syfuz):
    syfuz.add_cog(onlaunch(syfuz))
