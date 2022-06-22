import discord
import asyncio
import nacl
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="**")
client = discord.Client()

global quitting

@bot.event
async def on_ready():
    global quitting
    print("We have logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Game(name="학생들을 선동"))
    quitting = False

@bot.command()
async def join(ctx):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            await channel.connect()
            global quitting
            quitting = False
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아유! 음성채널에 먼저 가셔야죠 어머니!")
    except Exception as e:
        await ctx.send("이미 음성채널에 있다구요!")

@bot.command()
async def quit(ctx):
    await bot.voice_clients[0].disconnect()
    global quitting
    quitting = False
    await ctx.message.add_reaction("✅")

@bot.command()
async def stop(ctx):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
            server = ctx.message.guild
            channel = server.voice_client
            channel.stop()
            global quitting
            quitting = False
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아유! 음성채널에 먼저 가셔야죠 어머니!")
    except Exception as e:
        embed = discord.Embed(title="에러가 났다구요!", description=str(e), color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def 고자라니1(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani1.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 고자라니2(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani2.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 고자라니3(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani3.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 고자라니풀(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Gozarani_Full.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 반동(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Bandong.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 에엑따(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/EekTa.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 할거야안할거야(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Iwont.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 김두한(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/KimDooHan.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 안돼(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/No.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")
        
@bot.command()
async def 말도안돼(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/NoHorse.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 폭8(ctx):
    try:
        if not ctx.voice_client.is_playing():
            global quitting
            quitting = True
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Pokpal.mp3"))
            await ctx.message.add_reaction("✅")
            while ctx.voice_client.is_playing():
                await asyncio.sleep(0.01)
                if quitting:
                    pass
                else:
                   break
            if quitting:
                await bot.voice_clients[0].disconnect()
                await ctx.send(quitting)
                quitting = False
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 죄(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Sin.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 님(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/Socialism.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")

@bot.command()
async def 무슨소리(ctx):
    try:
        if not ctx.voice_client.is_playing():
            server = ctx.message.guild
            channel = server.voice_client
            channel.play(discord.FFmpegPCMAudio("./Sounds/WhatSound.mp3"))
            await ctx.message.add_reaction("✅")
        else:
            await ctx.send("아직 재생 중이라구요!")
    except:
        await ctx.send("아유! 음성채널에 먼저 초대해야 한다구요!")



access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)