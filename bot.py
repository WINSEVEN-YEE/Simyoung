import discord
import asyncio
import nacl
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="**")
client = discord.Client()

@bot.event
async def on_ready(ctx):
    print("We have logged in as {0.user}".format(bot))
    await ctx.send("저는 업데이트 됬다구요!")
    await bot.change_presence(activity=discord.Game(name="학생들을 선동"))

@bot.command()
async def join(ctx):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아유! 음성채널에 먼저 가셔야죠 어머니!")
    except Exception as e:
        await ctx.send("이미 음성채널에 있다구요!")

@bot.command()
async def quit(ctx):
    await bot.voice_clients[0].disconnect()
    await ctx.message.add_reaction("✅")

@bot.command()
async def 고자라니(ctx):
    server = ctx.message.guild
    channel = server.voice_client
    channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani.mp3"))
    await ctx.message.add_reaction("✅")

@bot.command()
async def 고자라니풀(ctx):
    server = ctx.message.guild
    channel = server.voice_client
    channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani_Full.mp3"))
    await ctx.message.add_reaction("✅")


access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)