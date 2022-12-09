import discord
from discord.ext import commands

class UserMention(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def usermention(self, ctx):
        await ctx.send(f"<@!{ctx.thread.id}> (`{ctx.thread.id}`)")

async def setup(bot):
    await bot.add_cog(UserMention(bot))
