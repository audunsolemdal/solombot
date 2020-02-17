import discord
import youtube_dl
import random
from discord.ext import commands
from discord.utils import get
import os


token = os.environ['TOKEN']
url = os.environ['URL']

print(token)
print(url)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('client running.')

@client.event
async def on_member_join(member):
    print('Tosken sjøl,' '{member}, has joined Tosken!')

@client.event
async def on_member_remove(member):
    print('Idioten,' '{member} has left Tosken')

@client.command(aliases=['commands', 'command'])
async def _help(context):
    helptext = "```"
    for command in client.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    await context.send(helptext)


@client.command(aliases=['git', 'github', 'contribute'])
async def _git(context):
    await context.send( 'Contribute @ https://github.com/solomson/solomclient')

@client.command(aliases=['watch', 'w2g'])
async def _w2g(context):
    await context.send(url)

@client.command(aliases=['bjarne'])
async def _bjarne(context):
    await context.send('BJARNE!!!')

@client.command(aliases=['8ball', 'g0mpball'])
async def _8ball(context):
    responses = [
        'Jepp',
        '100%'
    ]
    await context.send( random.choice(responses) )

@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The client has connected to {channel}\n")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The client has left {channel}")
    else:
        print("client was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

client.run(token)