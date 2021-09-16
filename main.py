import discord
from discord.ext import commands
import random
import sys
import os
import asyncio
import functools
import itertools
import math
import random
from async_timeout import timeout

token="token_here"

prefix='sf.'

syfuz=commands.Bot(command_prefix = prefix, case_insensitive=True)

syfuz.remove_command('help')
syfuz.remove_command('info')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        syfuz.load_extension(f'cogs.{filename[:-3]}')




syfuz.run(token)