import asyncio
import random
from asyncio import queues
import discord
import json
import shutil
import os
import datetime
import datetime, time
import io, random, json
from typing import Optional
from discord.ext import commands
from discord.utils import get
global mm

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

extensions = ['Cogs.administrator', 'Cogs.misc commands', 'Cogs.Help','Cogs.random','Cogs.time','Cogs.slots', 'Cogs.guide']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

#Welcome Message
@client.event
async def on_guild_join(guild, member):
    embed = discord.Embed(colour=0xeb144c, description=f"Welcome @{member} !\n\nAre you a __**Guest** __ or a __**Recruit**__?\n\nReact in #💬rules and get your Rank on the Server! \n\n__**Chairman's Club Guilds**__\n- Paragon\n- CrushFX\n- Silhouette\n- Hand of Doom\n- Rivers\n- AlphaOmega\n- Axi's Assassin's\n- The old Hunters\n- Brother Group")
    embed.set_image(url="https://cdn.discordapp.com/attachments/622516171442487306/730317391413772359/With_Axe_1_1.gif")
    embed.set_author(name="Who are you")
    embed.set_footer(text="Chairman's Club Administration", icon_url="https://cdn.discordapp.com/attachments/622516171442487306/730329581764214794/images.jpeg")

    channel = client.get_channel(id=726530916746395660)

    await channel.send(embed=embed)

#Roast Command
@client.command()
async def roast(ctx, member):
    responses = open('./roast.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(f'{response} {member}')

#Utility Commands
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Chairman´s Club"))
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

client.run("NzM3NjU0NjI3OTM1NDUzMTk2.XyAgaA.7RngJ0zuZhnwuAwjmZJNLWQ_yXQ")
