import discord
from discord.ext import commands
import traceback

import config

from cogs import mido_cmds
from cogs import mido_events

bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, status=discord.Status.invisible)

#configs
bot.token = config.BOT_TOKEN
bot.prefix = config.COMMAND_PREFIX
bot.custom_status = config.BOT_CUSTOM_STATUS
bot.status = config.BOT_STATUS
bot.s_role = config.ROLE_A
bot.c_role = config.ROLE_B
bot.k_role = config.ROLE_C
bot.a_role = config.ROLE_D
bot.men_role = config.ROLE_E
bot.women_role = config.ROLE_F
bot.secret_role = config.ROLE_G
bot.remove_command("help")

#bot on_ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Enabling.... Please Wait...."))
    print("[System] Startup...")
    
    names = ["mido_cmds", "mido_events"]
    
    try:
        for name in names:
            bot.load_extension(f"cogs.{name}")
            print(f"[System] File: {name} load Successfully.")
    except Exception as er:
        print(f"[System] File load failed. Show Error message...")
        print(f"[Error] {er}")
    
    if bot.status == "online":
        status = discord.Status.online
    elif bot.status == "idle":
        status = discord.Status.idle
    elif bot.status == "dnd":
        status = discord.Status.dnd
    elif bot.status == "offline":
        status = discord.Status.offline
    else:
        status = discord.Status.online
    
    if bot.custom_status is None:
        c_status = "A DiscordBot"
    else:
        c_status = bot.custom_status
    
    print("[System] Enabled!")
    await bot.change_presence(status=status, activity=discord.Game(name=c_status))

#help
@bot.command()
async def help(ctx):
    e = discord.Embed(title="Help Menu", color=0x2ecc71)
    e.add_field(name="introduction [nickname] [age] [s]", value=f"Introduction command.")
    await ctx.send(embed=e)

print("[System] Enabling.... Please Wait....")
bot.run(bot.token)