import asyncio
import random
from asyncio import queues
import discord
import youtube_dl
import json
import shutil
import os
from discord.ext import commands
from discord.utils import get
global mm

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

extensions = ['Cogs.administrator', 'Cogs.time', 'Cogs.random', 'Cogs.Music', 'Cogs.Activity', 'Cogs.Help', 'Cogs.slots']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

@client.command()
async def roast(ctx, member):
    responses = open('roast.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(f"{response} {member}")

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

@client.command()
async def on_ready(ctx):
    await client.change_presence(activity=discord.Game(name="Knighthood"))

print("Bot is ready!")
client.run("NzM3NjU0NjI3OTM1NDUzMTk2.XyAgaA.7RngJ0zuZhnwuAwjmZJNLWQ_yXQ")