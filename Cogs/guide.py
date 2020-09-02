import discord
from discord.ext import commands

class guide(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def easymaverick(self, ctx):
        await ctx.send("__**How to Farm easy Maverick Gauntlet**__\n\n"
                       "*If you wanna do it on the Pc install NOX or something like this and then go to :one: *\n\n"
                       ":one: Download an Autoclicker of your choice!! We used (picture below)\n\n"
                       "<https://cdn.discordapp.com/attachments/688713148311666704/733030111648940118/Screenshot_20200715-203908.jpg>\n\n"
                       ":two: Equip your **Strongest Weapon** and **Weakest Gauntlet** (Knight's gauntlet should always be good)\n\n"
                       ":three: Equip **Titania** (or a **Rage Power Heal Hero** of your choiche) on the __**RIGHT**__ slot (not the left)\n\n"
                       ":four: Head over to **Monster's cave** with **Kren Rockjow** in ROF !\n\n"
                       ":five: Start the Fight, **kill the side minions** and **place your Autoclicker** like this\n\n"
                       "<https://cdn.discordapp.com/attachments/661632045407141916/709479748291657819/Screenshot_20200511-205212__01.jpg>\n\n"
                       ":six: Start Autofarming and put a timer for **13 Minutes**, when the timer **Finishes Stop the Autofarming** and **Kill the Boss**!!\n\n"
                       ":seven: Proceding to the next stage and restarting from :five:\n\n"
                       ":eight: In the **3 Round** just Punch until it ends himself **dont Kill Kren Rockjow**!!\n\n")

    @commands.command()
    async def heroes(self, ctx):
        await ctx.send("<https://docs.google.com/spreadsheets/d/1OK9flOBhtmBQQcSeVjlr-s8wGI-0U569xSKShHLHfpY/edit#gid=0>")

    @commands.command()
    async def riddle(self, ctx):
        await ctx.send("__**Riddle Answers**__\n\n"
                       "Hunter of Astellan: ||Use Ash's rage power||\n"
                       "Notorious: ||Defeat Gorbash Thunderfist in a Monster Cave||\n"
                       "Unusually Ally: ||Use Balberith's base power||\n"
                       "The Sister: ||Defeat Sister Nona (Floor 3) of the Onslaught Dungeon||\n"
                       "Echoes in eternity: ||Win 10 Arena Battles||\n "
                       "Box of Delights: ||Open 20 chests||\n "
                       "The Lodge: ||Raid / Fight 20 hunts, any hunt is counted||\n "
                       "Around the world: ||Kill any 10 Roaming Monsters||\n "
                       "A Score of Skulls: ||kill 20 skeleton swordsman (highgard hunts)||\n "
                       "Simply Beastly: ||win 10 arena matches with a beast minion ||\n "
                       "The Worst: ||kill yellow deathweaver (highgard Spider roamer)||\n "
                       "Sacred Towers: ||finish 3 red favors||\n ")

    @commands.command()
    async def ahcalculator(self, ctx):
        await ctx.send("__**Basic Weapon and Armor/HP Calculator**__\n\n"
                       "In order to use this calculator, you have to __make a copy__ of it. It's still a work in progress, but right now you can use it to calculate:\n\n"
                       "- Your weapon's base damage and crit damage\n "
                       "- Your weapon's damage after factoring in gauntlet boost and crit charms\n"
                       "- How much armor/HP you'll have with more defense charms or full uniques etc.\n\n"
                       "*Made by Kazanci*\n\n"
                       "<https://docs.google.com/spreadsheets/d/1RHp9IOKhev4myvLbVCv2RYK_TwyHu9Qk_El8IK5Y-5A/edit#gid=0>")

    @commands.command()
    async def rofevent(self, ctx):
        await ctx.send("**How to clear RoF Event RM with objectives: Maniacal, Outlaw hero, Event wep**\n\n"
                       "This guide is only applicable for the stated objectives. You can beat this RM without using any pots by doing the following:\n\n"
                       "1. Maniacal gauntlet - Put __**blue**__ cores into **Hunter Speed** (Tristan & Krusa are hunters)\n"
                       "2. Outlaw hero - **Krusa**, ideally level 45 (max star preferable).\n"
                       "3. Healer - **Tristan**, level 45, max star (for Protect and Dispel).\n"
                       "4. Event weapon - Take whichever is at level 1\n\n"
                       "**⚔Strategy: Round 1⚔**\n"
                       "- Attack the demon only, using your lvl 1 weapon.\n"
                       "- Use Krusa's base whenever it's available to kill off the outlaws one-by-one.\n"
                       "- Use Tristan's base whenever it's available to stay at max health.\n"
                       "- When only the demon is left, punch it to death. Make sure Krusa's base is ready and you have at least two rounds of Protect up, before finishing the demon and going to Round 2.\n\n"
                       "**⚔Strategy: Round 2⚔**\n"
                       "- Same as above - attack the demon only, using your lvl 1 weapon.\n"
                       "- Use Krusa's base whenever it's available.\n"
                       "- Make sure Tristan's base is ready to dispel the burn from Varanus' rage.\n"
                       "- Once you've killed the back row, Krusa will target Varanus even though the demon to its left is still alive. You can now stunlock Varanus.\n"
                       "- You can choose to kill the outlaw to Varanus' right or let it Scarper. Just make sure to have Tristan's base ready if you decide to kill it.\n\n"
                       "That's all! Happy hunting ")

    @commands.command()
    async def malert(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/738658744656724018/image0-5.jpg")

    @commands.command()
    async def hrankup(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/738064840240791712/739063744801406986/unknown.png")

    @commands.command()
    async def gcore(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/738064840240791712/739063660114214912/unknown.png")

    @commands.command()
    async def dweapon(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729673817382846545/729674572131074068/INFOGRAPHIC_-_CHARM_-_WEAPON.png")

    @commands.command()
    async def darmor(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729673817382846545/729674660366647296/armordismantle.png")

    @commands.command()
    async def erankup(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/739045451772329984/739045481593962536/artej_equipmentRank2.png")

    @commands.command()
    async def mchart(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/737654987936497708/738854250712662066/image0.jpg")

    #Gauntlets
    @commands.command()
    async def grebel(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672676947525733/Basic_Guide.png")

    @commands.command()
    async def gchaotic(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672697868582932/02._BASIC_GUIDE_-_CHAOTIC_GAUNTLET.png")

    @commands.command()
    async def gmaverick(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672725660172298/03._BASIC_GUIDE_-_MAVERICK_GAUNTLET.png")

    @commands.command()
    async def gchampion(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672798813028392/04._BASIC_GUIDE_-_CHAMPION_GAUNTLET-1.png")

    @commands.command()
    async def gholy(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672819608256522/05._BASIC_GUIDE_-_HOLY_GAUNTLET.png")

    @commands.command()
    async def glogician(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672852718223411/06._BASIC_GUIDE_-_LOGICIAN_GAUNTLET-1.png")

    @commands.command()
    async def gmaniacal(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672886062678076/07._BASIC_GUIDE_-_MANIACAL_GAUNTLET.png")

    @commands.command()
    async def gvaliant(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672908967772200/08._BASIC_GUIDE_-_VALIANT_GAUNTLET.png")

    @commands.command()
    async def gdark(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672939901026434/09._BASIC_GUIDE_-_DARK_GAUNTLET.png")

    @commands.command()
    async def glawful(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/729672427507941447/729672992636010496/10._BASIC_GUIDE_-_LAWFUL_GAUNTLET.png")
    
    #Heroes
    @commands.command()
    async def Aeron(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614093795098691/Screenshot_20200703-072019_Knighthood.jpg")
        
    @commands.command()
    async def Alder(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728613850634649610/Screenshot_2020-07-03-12-31-10-127_com.king.knightsrage.jpg")        
        
    @commands.command()
    async def Anaara(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615278723727370/Screenshot_20200703-085857.png")
        
    @commands.command()
    async def Ash(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614175466717214/Screenshot_20200703-071950_Knighthood.jpg")
        
    @commands.command()
    async def Azhar(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/736203382842327150/image0.png")
        
    @commands.command()
    async def Balberith(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615826634047558/Screenshot_20200703-012957.png")        
        
    @commands.command()
    async def Balendu(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728628819367559238/Screenshot_20200703-170812.png")
        
    @commands.command()
    async def Blaine(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728937637770952744/Screenshot_20200704-081529_Knighthood.jpg")
                
    @commands.command()
    async def Byrne(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615612439330896/Screenshot_20200703-012912.png")
        
    @commands.command()
    async def Cladis(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615993127206944/Screenshot_20200703-013012.png")        
        
    @commands.command()
    async def Delphinia(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615548350627880/Screenshot_20200703-012857.png")
        
    @commands.command()
    async def Doctorflox(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728640145359765555/Screenshot_20200703-172845_Knighthood.jpg")
        
    @commands.command()
    async def Dondiego(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728625392344236162/Knighthood_2020-07-03-22-40-01.jpg")
        
    @commands.command()
    async def Dvalin(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615180220497930/Screenshot_20200703-085644.png")        
        
    @commands.command()
    async def Eileen(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614434309931078/Screenshot_20200703-182525_Knighthood.jpg")
        
    @commands.command()
    async def Ericson(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/728613262488502293/740271557921734717/image0.jpg")      
        
    @commands.command()
    async def Erinn(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728613770687021152/Screenshot_2020-07-03-12-31-17-366_com.king.knightsrage.jpg")
        
    @commands.command()
    async def Fahari(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728623170634121307/Knighthood_2020-07-03-22-40-26.jpg")        
        
    @commands.command()
    async def Garron(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/734150565105500311/743882865099669504/image0.jpg")
        
    @commands.command()
    async def Geber(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728841764835950613/image0-1.png")
        
    @commands.command()
    async def Grax(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615686288572466/Screenshot_20200703-012927.png")
        
    @commands.command()
    async def Grimm(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728618872671830036/Screenshot_20200703-173019.jpg")        
        
    @commands.command()
    async def Griz(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614523900133416/Screenshot_20200703-182510_Knighthood.jpg")
        
    @commands.command()
    async def Gunn(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614554782924840/Screenshot_20200703-182504_Knighthood.jpg")
                
    @commands.command()
    async def Gwen(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614661812912246/Screenshot_20200703-072054_Knighthood.jpg")
        
    @commands.command()
    async def Helmar(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614407659061309/Screenshot_20200703-013027.png")        
        
    @commands.command()
    async def Herne(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/734150565105500311/743882865795923988/image2.jpg")
        
    @commands.command()
    async def Isstara(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728620578445197402/image0-1.png")
        
    @commands.command()
    async def Kamil(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/734150565105500311/743883160328208455/image0.jpg")
        
    @commands.command()
    async def Keera(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728640089168805929/Screenshot_20200703-172837_Knighthood.jpg")        
        
    @commands.command()
    async def Krusa(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728623200589709402/Knighthood_2020-07-03-22-40-17.jpg")
        
    @commands.command()
    async def Lanasa(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/734150565105500311/743882865359585281/image1.jpg")
        
    @commands.command()
    async def Lance(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728613519913648188/Screenshot_2020-07-03-12-31-23-906_com.king.knightsrage.jpg")
        
    @commands.command()
    async def Lars(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614695069679707/Screenshot_20200703-072122_Knighthood.jpg")        
        
    @commands.command()
    async def Logan(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614496557334558/Screenshot_20200703-182514_Knighthood.jpg")
        
    @commands.command()
    async def Lukin(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/734150565105500311/743883236106698952/image0.jpg")
        
    @commands.command()
    async def MacLeod(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728698010938376272/Screenshot_20200703-213637.png")
        
    @commands.command()
    async def Millicent(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614805874933820/Screenshot_20200703-165839_Knighthood.jpg")        
        
    @commands.command()
    async def Neko(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728959876973330482/Screenshot_20200704-194406_Knighthood.png")
        
    @commands.command()
    async def Nijuro(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615146326589550/Screenshot_20200703-085458.png")
                
    @commands.command()
    async def Olaf(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615416741625876/Screenshot_20200703-012818.png")
        
    @commands.command()
    async def Outis(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/729054269373677578/Screenshot_20200705-022002_Knighthood.png")        
        
    @commands.command()
    async def Pentatonix(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615495149945002/Screenshot_20200703-012834.png")
        
    @commands.command()
    async def Rhiannon(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615225330368552/Screenshot_20200703-085553.png")
        
    @commands.command()
    async def Rokara(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614015407751258/Screenshot_20200703-072042_Knighthood.jpg")
        
    @commands.command()
    async def Rosalin(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614142910529576/Screenshot_20200703-072005_Knighthood.jpg")        
        
    @commands.command()
    async def Serra(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728959928458281021/Screenshot_20200704-194302_Knighthood.png")
        
    @commands.command()
    async def Sola(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728632216309072003/Screenshot_20200703-121935_Knighthood.jpg")      
        
    @commands.command()
    async def Tara(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615767611801610/Screenshot_20200703-012950.png")
        
    @commands.command()
    async def Titania(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615319677173800/Screenshot_20200703-085945.png")        
        
    @commands.command()
    async def Tristan(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615885237125201/Screenshot_20200703-013005.png")
        
    @commands.command()
    async def Ulfred(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615446584098926/Screenshot_20200703-012826.png")
        
    @commands.command()
    async def Ursula(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615578138574928/Screenshot_20200703-012905.png")
        
    @commands.command()
    async def Viktor(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615649273839646/Screenshot_20200703-012920.png")        
        
    @commands.command()
    async def Vordrai(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615119319466004/Screenshot_20200703-085326.png")
        
    @commands.command()
    async def Weifeng(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/736172266366173254/Screenshot_20200724-123004_Knighthood.jpg")
                
    @commands.command()
    async def Wormwood(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728845959303266364/image0-2.png")
        
    @commands.command()
    async def Zalam(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728614729379086397/Screenshot_20200703-072105_Knighthood.jpg")        
        
    @commands.command()
    async def Zoe(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728613262488502293/728615723982782464/Screenshot_20200703-012935.png")
    
    #Minions
    @commands.command()
    async def Bear(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869595057881138/Screenshot_20200704-085515_Knighthood.jpg")        
 
    @commands.command()
    async def Vargr(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869660514320444/Screenshot_20200704-085510_Knighthood.jpg")               
        
    @commands.command()
    async def Commander(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728870425794183278/Screenshot_20200704-085347_Knighthood.jpg")        
        
    @commands.command()
    async def Fleshcrusher(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728893602385756160/Screenshot_20200704-085422_Knighthood.jpg")        
        
    @commands.command()
    async def Tanker(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728893560685854760/Screenshot_20200704-085414_Knighthood.jpg")         
        
    @commands.command()
    async def Longhorn(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728868420799430666/Screenshot_20200704-095637.jpg")        
 
    @commands.command()
    async def Bowmaster(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728870316180504636/Screenshot_20200704-085402_Knighthood.jpg")               
        
    @commands.command()
    async def Loremaster(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728867301859917824/Screenshot_20200704-095627.jpg")        
        
    @commands.command()
    async def Hog(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869623839064064/Screenshot_20200704-085519_Knighthood.jpg")        
        
    @commands.command()
    async def Parrot(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869561276825640/Screenshot_20200704-085523_Knighthood.jpg")           
        
    @commands.command()
    async def Initiate(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869028059414538/Screenshot_20200704-085528_Knighthood.jpg")        
 
    @commands.command()
    async def Centurion(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728868938925998160/Screenshot_20200704-085534_Knighthood.jpg")               
        
    @commands.command()
    async def Stormbringer(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728868546591064124/Screenshot_20200704-095646.jpg")        
        
    @commands.command()
    async def Knifer(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869942090399744/Screenshot_20200704-085431_Knighthood.jpg")        
        
    @commands.command()
    async def Clobberer(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869816118542386/Screenshot_20200704-085427_Knighthood.jpg")           
        
    @commands.command()
    async def Mender(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728870216871837736/Screenshot_20200704-085440_Knighthood.jpg")        
 
    @commands.command()
    async def Matriarch(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728870381238353930/Screenshot_20200704-085353_Knighthood.jpg")               
        
    @commands.command()
    async def Fenfolk(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728868074345857044/Screenshot_20200704-095652.jpg")        
        
    @commands.command()
    async def Draughtmaster(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728870243375513621/Screenshot_20200704-085406_Knighthood.jpg")        
        
    @commands.command()
    async def Deadeye(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728868646537003080/Screenshot_20200704-095632.jpg")           
        
    @commands.command()
    async def Drake(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728875430597361694/Screenshot_20200704-085418_Knighthood.jpg") 
        
    @commands.command()
    async def Spider(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728870349613039636/Screenshot_20200704-085358_Knighthood.jpg")         
        
    @commands.command()
    async def Stonesmasher(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728869763421569044/Screenshot_20200704-085448_Knighthood.jpg") 
        
    @commands.command()
    async def Flameslinger(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/728864840118173746/728866227295879268/Screenshot_20200703-225130_Knighthood.jpg")          
        
               
def setup(bot):
    bot.add_cog(guide(bot))
