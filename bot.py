import discord
import asyncio
import nacl
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="**")
client = discord.Client()

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Game(name="학생들을 선동"))

@bot.command()
async def join(ctx):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
            if discord.utils.get(client.voice_clients, guild=ctx.guild) != None:
                channel = ctx.author.voice.channel
                await channel.connect()
                await ctx.message.add_reaction("✅")
            else:
                await ctx.send("이미 음성채널에 있다구요!")
        else:
            await ctx.send("아유! 음성채널에 먼저 가셔야죠 어머니!")
    except Exception as e:
        elog = str(e)
        embed = discord.Embed(title="에러가 났다구요!", description=elog, color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def quit(ctx):
    if discord.utils.get(client.voice_clients, guild=ctx.guild) == None:
        await bot.voice_clients[0].disconnect()
        await ctx.message.add_reaction("✅")
    else:
        await ctx.send("이미 음성채널에 없다구요!")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)