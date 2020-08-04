import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xffffff), description="__**Other**__\n`user`, `division`, `multiply`, `subtract`, `calculate`\n\n__**Guides**__\n`hguides`\n\n__**Fun**__\n`8ball`, `slots`, `roast`\n\n__**Admin**__\n`say`, `clear`, `kick`, `ban`, `unban`, `mute`, `unmute`\n\n__**Utility**__\n`time`, `ping`, `uptime`")
        embed.set_author(name="Chairman´s Bot Help List")
        embed.set_footer(text="Chairman´s Bot Version Beta")

        await ctx.send(embed=embed)

    @commands.command()
    async def hguides(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xffffff), description="\n__**1. Minions Guide**__\n-Where to find minions and which gauntlet to use? Type: .malert or .mchart\n\n__**2. Gauntlets Guide**__\n-For **Rebel Gauntlet** Type: .grebel\n\n-For **Chaotic Gauntlet** Type: .gchaotic\n\n-For **Maverick Gauntlet** Type: .gmaverick\n\n-For **Holy Gauntlet** Type: .gholy\n\n-For **Lawful Gauntlet** Type: .glawful\n\n-For **Logician Gauntlet** Type: .glogician\n\n-For **Dark Gauntlet** Type: .gdark\n\n-For **Champion Gauntlet** Type: .gchampion\n\n-For **Valiant Gauntlet** Type: .gvaliant\n\n-For **Maniacal Gauntlet** Type: .gmaniacal\n\n__**3. Equipment**__\nInfo on **Dismantle Weapon** Type: .dweapon\n\nInfo on **Dismantle Armor** Type: .darmor\n\nInfo on **Gauntlet Core** Amount Type: .gcore\n\nInfo on **Equimpent Rank up Resource Amount** Type: .erankup\n\nInfo on **Hero Rank up Resource Amount** Type: .hrankup")
        embed.set_author(name="Chairman´s Bot Guide List")
        embed.set_footer(text="Chairman´s Bot Version Beta")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
