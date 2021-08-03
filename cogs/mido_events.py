import discord
from discord.ext import commands

class mido_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"[Error] {error}")
        await ctx.send(embed=discord.Embed(title="Unexpected Error!!", description=f"```py\n{error}\n```", color=0x2ecc71))

def setup(bot):
    bot.add_cog(mido_events(bot))