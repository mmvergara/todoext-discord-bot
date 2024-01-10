from discord.ext import commands

class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def show(self, ctx):
        await ctx.send('Showing all projects')

async def setup(bot):
    await bot.add_cog(MyCommands(bot))
