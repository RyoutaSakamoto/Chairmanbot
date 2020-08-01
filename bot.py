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

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Chairman´s Club"))
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

@client.command()
async def malert(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/738658744656724018/image0-5.jpg")

@client.command()
async def erura(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/643826426415546387/738673749678882896/artej_equipmentRank.png")

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

	
@client.command()
async def roast(ctx, member):
    responses = open('./roast.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(f'{response} {member}')

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
@commands.has_permissions(ban_members=True)
async def softban(ctx, member : discord.Member, *, reason=None):
    if not member:
        return await ctx.send("You must specify a user")

    try:
        await member.ban(reason=None)
        await member.unban()
        await ctx.send(f'{member.mention} Has been banned & unbanned')
    except discord.Forbidden:
        return await ctx.send("forbidden")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int): #(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'kicked{member.mention}')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Forbidden {member.mention}')


@client.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member:discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} User{} Was muted" .format(member.mention,ctx.author.mention))
            return

            overwrite = discord.PermissionOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{}  User {} Was muted" .format(member.mention,ctx.author.mention))

@client.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member:discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} The User Was Unmuted" .format(member.mention))
        return

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Chairman´s Bot command List", color=0x000000)
    embed.add_field(name="other", value="`user`, `division`, `multiply`, `subtract`, `calculate`",)
    embed.add_field(name="guides", value="`hguides`",)
    embed.add_field(name="fun", value="`8ball`, `slots`, `roast`",)
    embed.add_field(name="admin", value="`say`, `clear`, `kick`, `ban`, `unban`, `mute`, `unmute`",)
    embed.add_field(name="utility", value="`time`, `ping`, `uptime`",)
    await ctx.send(embed=embed)

@client.command()
async def hguides(ctx):
    embed = discord.Embed(title="Chairman´s Bot Guide List", color=0x000000)
    embed.add_field(name="1. Minions Guide", value="-Where to find minions and which gauntlet to use? Type .malert",)
    embed.add_field(name="2. Gauntlets Guide", value="-For Rebel Gauntlet Type: .grebel"
                                                     "-For Chaotic Gauntlet Type: .gchaotic"
                                                     "-For Maverick Gauntlet Type: .gmaverick"
                                                     "-For Holy Gauntlet Type: .gholy"
                                                     "-For Lawful Gauntlet Type: .glawful"
                                                     "-For Logician Gauntlet Type: .glogician"
                                                     "-For Dark Gauntlet Type: .gdark"
                                                     "-For Champion Gauntlet Type: .gchampion"
                                                     "-For Valiant Gauntlet Type: .gvaliant"
                                                     "-For Maniacal Gauntlet Type: .gmaniacal ")
   embed.add_field(name="3. Equipment", value="Info on Resource amount needed to level up type - .mchart",)
		    
@client.command(name='8ball',
            description="Answers a yes/no question.",
            brief="Answers from the beyond.",
            aliases=['eight_ball', 'eightball', '8-ball'],
            pass_context=True)

async def eight_ball(context):
    possible_responses = [

        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Maybe so',
	'SERIOUSLY....you already know the answer from Google and you still ask me. Why not asking Google,'
	'Nah, im just a machine. Pip...Pop...Pip...Pi...Di..Pop...',
	'Wait...Lets me ask my friend Google real quick',
	'Ah...These questions again...Why did you created me',   

    ]
    await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)
	
@client.command()
async def say(ctx,*,msg):
    await ctx.message.delete()
    await ctx.send("{}" .format(msg))

@client.command()
async def calculate(ctx, a:int, b:int):
    await ctx.send(a+b)

@client.command()
async def subtract(ctx, a:int, b:int):
    await ctx.send(a-b)

@client.command()
async def multiply(ctx, a:int, b:int):
    await ctx.send(a*b)

@client.command()
async def division(ctx, a:int, b:int):
    if b==0:
        ans="0"
    else:
        ans=a/b
    await ctx.send(ans)

@client.command()
async def slots(ctx):
    """!slots - Play fruit emojis slot machine."""
    icon_url = 'https://i.imgur.com/8oGuoyq.png'
    slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
    slot1 = slots[random.randint(0, 5)]
    slot2 = slots[random.randint(0, 5)]
    slot3 = slots[random.randint(0, 5)]
    slot4 = slots[random.randint(0, 5)]

    slot_spin = f'|\t:{slot1}:\t|\t:{slot2}:\t|\t:{slot3}:\t|\t:{slot4}:\t|'
    jackpot = '$$$ !!! JACKPOT !!! $$$'

    embed = discord.Embed(colour=discord.Colour.gold())
    embed.set_author(name='Slot Machine', icon_url=icon_url)
    embed.add_field(
        name=f'*{ctx.author.name} pulls the slot machine handle...*',
        value='\u200b',
        inline=False,

    )

    if (
            slot1 == slot2 and slot3 == slot4 or
            slot1 == slot3 and slot2 == slot4 or
            slot1 == slot4 and slot2 == slot3
    ):
        embed.add_field(name=slot_spin, value='\u200b')
        embed.set_footer(text=jackpot)
    else:
        embed.add_field(name=slot_spin, value='\u200b')
    await ctx.send(embed=embed)

start_time = datetime.datetime.now()

@client.command()
async def time(ctx):
	current_time = datetime.datetime.now().strftime('%H:%M:%S')
	embed = discord.Embed(color=0xB2272D)
	embed.add_field(name=':alarm_clock: Time:', value=(f'Current time is: {current_time}'), inline=True)
	await ctx.send(embed=embed)

@client.command()
async def uptime(ctx):
	current_time = datetime.datetime.now()
	difference = current_time - start_time
	text = difference.total_seconds() / 3600
	await ctx.send('Current uptime: {:.2f} hours'.format(text))

client.run("NzM3NjU0NjI3OTM1NDUzMTk2.XyAgaA.7RngJ0zuZhnwuAwjmZJNLWQ_yXQ")
