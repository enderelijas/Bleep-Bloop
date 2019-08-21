import discord
from discord.ext import commands
import random
import os


bot = commands.Bot ("c.")

@bot.event
async def on_ready():
    print("Bot online")


@bot.command()
async def spam(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value='sapm')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong :stuck_out_tongue_closed_eyes: ")


bot.run(os.getenv('TOKEN')) 
