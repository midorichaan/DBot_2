import discord
from discord.ext import commands

import traceback

class mido_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #introduction
    @commands.command(aliases=["intro"], description="Introduction command.", usage="<prefix>introduction [nickname] [age] [sex]")
    async def introduction(self, ctx, nick=None, age:int=None, s:int=None):
        bot = self.bot
        
        if nick == None:
            nick = ctx.author.name
        else:
            nick = nick
        
        if age is None:
            print("[Error] MissingRequiredArgument.")
            raise commands.MissingRequiredArgument(age)
        elif 8 < age and age < 13:
            role = bot.s_role
        elif 14 < age and age < 16:
            role = bot.c_role
        elif 17 < age and age < 19:
            role = bot.k_role
        elif age >= 20:
            role = bot.a_role
        else:
            print(f"[Error] Invailed argument.")
            raise TypeError("Invailed argument.")
        
        if s is None:
            print(f"[Error] MissingRequiredArgument Error.")
            raise commands.MissingRequiredArgument(s)
        elif s == 0:
            role2 = self.bot.men_role
        elif s == 1:
            role2 = self.bot.women_role 
        elif s == 2:
            role2 = self.bot.secret_role
        else:
            print(f"[Error] Invailed argument.")
            raise TypeError("Invailed argument.")
        
        try:
            await ctx.author.add_roles(ctx.guild.get_role(role), ctx.guild.get_role(role2), reason="Introduction Successfully")
            await ctx.author.edit(nick=nick)
            return await ctx.send("Done!")
        except Exception as er:
            print(f"[Error] {er}")
            raise commands.CommandInvokeError(er)

def setup(bot):
    bot.add_cog(mido_cmds(bot))