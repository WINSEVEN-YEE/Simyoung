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
async def 고자라니1(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani1.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 고자라니2(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani2.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 고자라니3(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani3.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 고자라니풀(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani_Full.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 반동(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Bandong.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 에엑따(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/EekTa.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 할거야안할거야(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Iwont.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 김두한(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/KimDooHan.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 안돼(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/No.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")
        
@bot.command()
async def 말도안돼(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/NoHorse.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 폭8(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Pokpal.mp3"))
        await ctx.message.add_reaction("✅")
        while ctx.voice_client.is_playing():
            pass
        await bot.voice_clients[0].disconnect()
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 죄(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Sin.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 님(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/Socialism.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 무슨소리(ctx):
    try:
        server = ctx.message.guild
        channel = server.voice_client
        channel.play(discord.FFmpegPCMAudio("./Sounds/WhatSound.mp3"))
        await ctx.message.add_reaction("✅")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")



access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)