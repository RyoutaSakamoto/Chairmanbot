import discord
from discord.ext import commands


class guides(commands.Cog):
    
    @commands.command()
    async def malert(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/738658744656724018/image0-5.jpg")

    @commands.command()
    async def hrankup(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/738064840240791712/739063744801406986/unknown.png")

    @commands.command()
    async def gcore(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/738064840240791712/739063660114214912/unknown.png")

    @commands.command()
    async def dweapon(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729673817382846545/729674572131074068/INFOGRAPHIC_-_CHARM_-_WEAPON.png")

    @commands.command()
    async def darmor(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729673817382846545/729674660366647296/armordismantle.png")
    
    @commands.command()
    async def erankup(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/739045451772329984/739045481593962536/artej_equipmentRank2.png")

    @commands.command()
    async def mchart(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/737654987936497708/738854250712662066/image0.jpg")

    @commands.command()
    async def grebel(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672676947525733/Basic_Guide.png")

    @commands.command()
    async def gchaotic(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672697868582932/02._BASIC_GUIDE_-_CHAOTIC_GAUNTLET.png")

    @commands.command()
    async def gmaverick(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672725660172298/03._BASIC_GUIDE_-_MAVERICK_GAUNTLET.png")

    @commands.command()
    async def gchampion(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672798813028392/04._BASIC_GUIDE_-_CHAMPION_GAUNTLET-1.png")

    @commands.command()
    async def gholy(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672819608256522/05._BASIC_GUIDE_-_HOLY_GAUNTLET.png")

    @commands.command()
    async def glogician(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672852718223411/06._BASIC_GUIDE_-_LOGICIAN_GAUNTLET-1.png")

    @commands.command()
    async def gmaniacal(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672886062678076/07._BASIC_GUIDE_-_MANIACAL_GAUNTLET.png")

    @commands.command()
    async def gvaliant(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672908967772200/08._BASIC_GUIDE_-_VALIANT_GAUNTLET.png")

    @commands.command()
    async def gdark(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672939901026434/09._BASIC_GUIDE_-_DARK_GAUNTLET.png")
    
    @commands.command()
    async def glawful(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672992636010496/10._BASIC_GUIDE_-_LAWFUL_GAUNTLET.png")

def setup(bot):
    bot.add_cog(guides(bot))
