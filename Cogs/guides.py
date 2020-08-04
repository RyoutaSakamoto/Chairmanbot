import discord
from discord.ext import commands


class Activity(commands.Cog):

def setup(bot):
    bot.add_cog(guides(bot))
