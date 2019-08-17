import discord
from discord.ext import commands
import random


bot = commands.Bot ("c.")

@bot.event
async def on_ready():
    print("Bot online")


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong :stuck_out_tongue_closed_eyes: ")


bot.run(os.getenv('TOKEN')) 
