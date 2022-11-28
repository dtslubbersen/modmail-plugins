import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class ID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def id(self, ctx):
        await ctx.send(ctx.thread.id)
        
async def setup(bot):
  await bot.add_cog(ID(bot)
