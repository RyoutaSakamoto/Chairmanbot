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

extensions = ['Cogs.administrator', 'Cogs.misc commands', 'Cogs.Help','Cogs.random','Cogs.time','Cogs.slots']

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

#Guide Commands
@client.command()
async def malert(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/738658744656724018/image0-5.jpg")

@client.command()
async def hrankup(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/738064840240791712/739063744801406986/unknown.png")

@client.command()
async def gcore(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/738064840240791712/739063660114214912/unknown.png")

@client.command()
async def dweapon(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729673817382846545/729674572131074068/INFOGRAPHIC_-_CHARM_-_WEAPON.png")

@client.command()
async def darmor(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729673817382846545/729674660366647296/armordismantle.png")

@client.command()
async def erankup(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/739045451772329984/739045481593962536/artej_equipmentRank2.png")

@client.command()
async def mchart(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/737654987936497708/738854250712662066/image0.jpg")

@client.command()
async def grebel(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672676947525733/Basic_Guide.png")

@client.command()
async def gchaotic(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672697868582932/02._BASIC_GUIDE_-_CHAOTIC_GAUNTLET.png")

@client.command()
async def gmaverick(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672725660172298/03._BASIC_GUIDE_-_MAVERICK_GAUNTLET.png")

@client.command()
async def gchampion(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672798813028392/04._BASIC_GUIDE_-_CHAMPION_GAUNTLET-1.png")

@client.command()
async def gholy(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672819608256522/05._BASIC_GUIDE_-_HOLY_GAUNTLET.png")

@client.command()
async def glogician(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672852718223411/06._BASIC_GUIDE_-_LOGICIAN_GAUNTLET-1.png")

@client.command()
async def gmaniacal(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672886062678076/07._BASIC_GUIDE_-_MANIACAL_GAUNTLET.png")

@client.command()
async def gvaliant(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672908967772200/08._BASIC_GUIDE_-_VALIANT_GAUNTLET.png")

@client.command()
async def gdark(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672939901026434/09._BASIC_GUIDE_-_DARK_GAUNTLET.png")

@client.command()
async def glawful(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672992636010496/10._BASIC_GUIDE_-_LAWFUL_GAUNTLET.png")

#Utility Commands
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Chairman´s Club"))
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

@client.command()
async def ping(ctx):
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f'Pong! That took {1000 * diff.total_seconds():.1f}ms.')

@client.command()
async def user(ctx, member: discord.Member = None):
    '''Display informations about given user'''
    member = ctx.author if not member else member

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:', value=member.id)
    embed.add_field(name="Name:", value=member.display_name)
    embed.add_field(name='Acount created at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name="Joined the server:", value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name=f'Roles({len(roles)}):', value=''.join([role.mention for role in roles]))

    await ctx.send(embed=embed)

client.run("NzM3NjU0NjI3OTM1NDUzMTk2.XyAgaA.7RngJ0zuZhnwuAwjmZJNLWQ_yXQ")
