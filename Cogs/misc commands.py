import discord
import json, random, datetime, time, urllib.request, io, os, aiohttp

from typing import Union
from discord.ext import commands
from discord.utils import get
from random import randint

global mm

class misccommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['пинг'])
    async def ping(self,ctx):
        resp = await ctx.send('Pong! Loading...')
        diff = resp.created_at - ctx.message.created_at
        await resp.edit(content=f'Pong! That took {1000 * diff.total_seconds():.1f}ms.')

    @commands.command()
    async def gotrek(self, ctx):
        await ctx.send("https://tenor.com/view/what-dog-doggo-star-trek-spock-gif-5972496")

    @commands.command()
    async def hotdog(self, ctx):
        await ctx.send("https://tenor.com/view/hotdog-running-doggy-gif-15413180")

    @commands.command()
    async def chicken(self, ctx):
        await ctx.send("https://tenor.com/view/saki-nikaido-%e4%ba%8c%e9%9a%8e%e5%a0%82%e3%82%b5%e3%82%ad-zombie-land-saga-%e3%82%be%e3%83%b3%e3%83%93%e3%83%a9%e3%83%b3%e3%83%89%e3%82%b5%e3%82%ac-anime-gif-12807826")

    @commands.command()
    async def dead(self, ctx):
        await ctx.send("https://tenor.com/view/dead-inside-anime-loveiswar-kaguya-gif-13628541")

    @commands.command()
    async def alive(self, ctx):
        await ctx.send("https://tenor.com/view/anime-okay-then-meh-unamused-nom-gif-18015248")

    @commands.command(name='8ball',
            description="Answers a yes/no question.",
            brief="Answers from the beyond.",
            aliases=['eight_ball', 'eightball', '8-ball'],
            pass_context=True)
    async def eight_ball(self, ctx, context):
        possible_responses = ['That is a resounding no',
                              'It is not looking likely',
                              'Too hard to tell',
                              'It is quite possible',
                              'Definitely',
                              'Maybe so',
                              'SERIOUSLY....you already know the answer from Google and you still ask me. Why not asking Google,'
                              'Nah, im just a machine. Pip...Pop...Pip...Pi...Di..Pop...',
                              'Wait...Lets me ask my friend Google real quick',
                              'Ah...These questions again...Why did you created me',]
	
        await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)

    @commands.command(aliases=['сказать' , 'сказ'])
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send("{}" .format(msg))

    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
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

    @commands.command()
    async def calculate(self, ctx, a:int, b:int):
        await ctx.send(a+b)

    @commands.command()
    async def subtract(self, ctx, a:int, b:int):
        await ctx.send(a-b)

    @commands.command()
    async def multiply(self, ctx, a:int, b:int):
        await ctx.send(a*b)

    @commands.command()
    async def division(self, ctx, a:int, b:int):
        if b==0:
            ans="0"
        else:
            ans=a/b
        await ctx.send(ans)

    @commands.command()
    async def memo(self,ctx, a:str):
        global mm
        mm=a
        await ctx.send("okay")


    @commands.command()
    async def remind(self,ctx):
        await ctx.send(mm)

    @commands.command(name='bigemoji')
    async def get_emoji_url(self, ctx, emoji: Union[discord.Emoji, discord.PartialEmoji, str]):
        """Sends a big version of an emoji and it's URL of available"""
        if isinstance(emoji, (discord.Emoji, discord.PartialEmoji)):
            await ctx.send(str(emoji.url))
        else:
            await ctx.send(emoji)

def setup(bot):
    bot.add_cog(misccommands(bot))
