import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xffffff), description="📣__**Other**__"
                                                                           "\n- user"
                                                                           "\n- memo"
                                                                           "\n- randnumber"
                                                                           "\n- choice"
                                                                           "\n- roll"
                                                                           "\n- division"
                                                                           "\n- multiply"
                                                                           "\n- subtract"
                                                                           "\n- calculate\n\n"
                                                                           "🌀__**Guides**__"
                                                                           "\n- hguides\n\n"
                                                                           "🃏__**Fun**__"
                                                                           "\n- 8ball"
                                                                           "\n- slots"
                                                                           "\n- roast"
                                                                           "\n- dead"
                                                                           "\n- alive"
                                                                           "\n- chicken"
                                                                           "\n- hotdog\n\n"
                                                                           "💈__**Admin**__"
                                                                           "\n- say"
                                                                           "\n- softban"
                                                                           "\n- clear"
                                                                           "\n- kick"
                                                                           "\n- ban"
                                                                           "\n- unban"
                                                                           "\n- mute"
                                                                           "\n- unmute\n\n"
                                                                           "🕐__**Utility**__"
                                                                           "\n- time"
                                                                           "\n- ping"
                                                                           "\n- remind"
                                                                           "\n- uptime")
        embed.set_author(name="Akari Bot Help List")
        embed.set_footer(text="Akari Bot Version (1.0.0)")
        await ctx.send(embed=embed)

    @commands.command()
    async def hguides(self, ctx):

        embed = discord.Embed(colour=discord.Colour(0xffffff), description="\n🙈 __**1. Minions Guide**__\n\n"
                                                                           "-Where to find **Minions** and which gauntlet to use? Type: .malert or .mchart\n\n"
                                                                           "- All **Minions** (First Letter big + Second Name for the Minion) Type: .[Minion Name]\n\n"
                                                                           "📕__**2. Gauntlets Guide**__\n\n"
                                                                           "- For **Rebel Gauntlet** Type: .grebel\n\n"
                                                                           "- For **Chaotic Gauntlet** Type: .gchaotic\n\n"
                                                                           "- For **Maverick Gauntlet** Type: .gmaverick\n\n"
                                                                           "- For **Holy Gauntlet** Type: .gholy\n\n"
                                                                           "- For **Lawful Gauntlet** Type: .glawful\n\n"
                                                                           "- For **Logician Gauntlet** Type: .glogician\n\n"
                                                                           "- For **Dark Gauntlet** Type: .gdark\n\n"
                                                                           "- For **Champion Gauntlet** Type: .gchampion\n\n"
                                                                           "- For **Valiant Gauntlet** Type: .gvaliant\n\n"
                                                                           "- For **Maniacal Gauntlet** Type: .gmaniacal\n\n"
                                                                           "🔰__**3. Equipment**__\n\n"
                                                                           "- Info on **Dismantle Weapon** Type: .dweapon\n\n"
                                                                           "- Info on **Dismantle Armor** Type: .darmor\n\n"
                                                                           "- Info on **Gauntlet Core** Amount Type: .gcore\n\n"
                                                                           "- Info on **Equimpent Rank up Resource Amount** Type: .erankup\n\n"
                                                                           "- Info on **Hero Rank up Resource Amount** Type: .hrankup\n\n"
                                                                           "🦸__**4. Heroes**__\n\n"
                                                                           "- All **Heroes** (First Letter big) Type: .[Heores Name]\n\n"
                                                                           "- Knighthood **Heroes** Sheet Type: .heroes\n\n"
                                                                           "🎫__**5.Other**__\n\n"
                                                                           "- How to kill the **RoF Event Roaming Monster** Type: .rofevent\n\n"
                                                                           "- Basic **Weapon and Armor/HP** Calculator Type: .ahcalculator\n\n"
                                                                           "- Get all **Riddle Answer** Type: .riddle\n\n"
                                                                           "- Farm easy the **Maverick Gauntlet** Type .easymaverick")
        embed.set_author(name="Akari Bot Help List")
        embed.set_footer(text="Akari Bot Version (1.0.0)")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
