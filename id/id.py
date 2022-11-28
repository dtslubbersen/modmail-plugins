import discord
from discord.ext import commands

class ThreadID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def id(self, ctx):
        await ctx.send(ctx.thread.id)

async def setup(bot):
    await bot.add_cog(ThreadID(bot))
