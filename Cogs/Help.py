import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xffffff), description="__**Other**__\n"
                                                                           "`user`,"
                                                                           "`memo`,"
                                                                           "`randnumber`,"
                                                                           "`choice`,"
                                                                           "`roll`, "
                                                                           "`division`, "
                                                                           "`multiply`, "
                                                                           "`subtract`, "
                                                                           "`calculate`\n\n"
                                                                           "__**Guides**__\n"
                                                                           "`hguides`\n\n"
                                                                           "__**Fun**__\n"
                                                                           "`8ball`, "
                                                                           "`slots`, "
                                                                           "`roast`\n\n"
                                                                           "__**Admin**__\n"
                                                                           "`say`,"
                                                                           "`softban`, "
                                                                           "`clear`, "
                                                                           "`kick`, "
                                                                           "`ban`, "
                                                                           "`unban`, "
                                                                           "`mute`, "
                                                                           "`unmute`\n\n"
                                                                           "__**Utility**__\n"
                                                                           "`time`, "
                                                                           "`ping`,"
                                                                           "`remind`, "
                                                                           "`uptime`")
        embed.set_author(name="Chairman´s Bot Help List")
        embed.set_footer(text="Chairman´s Bot Version Beta")

        await ctx.send(embed=embed)

    @commands.command()
    async def hguides(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xffffff), description="\n__**1. Minions Guide**__\n"
                                                                           "-Where to find **Minions** and which gauntlet to use? Type: .malert or .mchart\n\n"
                                                                           "-All **Minions** (First Letter big + Second Name for the Minion) Type: .[Minion Name]\n\n"
                                                                           "__**2. Gauntlets Guide**__\n\n"
                                                                           "-For **Rebel Gauntlet** Type: .grebel\n\n"
                                                                           "-For **Chaotic Gauntlet** Type: .gchaotic\n\n"
                                                                           "-For **Maverick Gauntlet** Type: .gmaverick\n\n"
                                                                           "-For **Holy Gauntlet** Type: .gholy\n\n"
                                                                           "-For **Lawful Gauntlet** Type: .glawful\n\n"
                                                                           "-For **Logician Gauntlet** Type: .glogician\n\n"
                                                                           "-For **Dark Gauntlet** Type: .gdark\n\n"
                                                                           "-For **Champion Gauntlet** Type: .gchampion\n\n"
                                                                           "-For **Valiant Gauntlet** Type: .gvaliant\n\n"
                                                                           "-For **Maniacal Gauntlet** Type: .gmaniacal\n\n"
                                                                           "__**3. Equipment**__\n"
                                                                           "Info on **Dismantle Weapon** Type: .dweapon\n\n"
                                                                           "Info on **Dismantle Armor** Type: .darmor\n\n"
                                                                           "Info on **Gauntlet Core** Amount Type: .gcore\n\n"
                                                                           "Info on **Equimpent Rank up Resource Amount** Type: .erankup\n\n"
                                                                           "Info on **Hero Rank up Resource Amount** Type: .hrankup\n\n"
                                                                           "__**4. Heroes**__\n"
                                                                           "-All **Heroes** (First Letter big) Type: .[Heores Name]")
        embed.set_author(name="Chairman´s Bot Guide List")
        embed.set_footer(text="Chairman´s Bot Version Beta")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
