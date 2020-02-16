import discord
import random
from discord.ext import commands
import os


token = os.environ['TOKEN']
url = os.environ['URL']

print(token)
print(url)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot running.')

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
    await context.send( 'Contribute @ https://github.com/solomson/solombot')

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

client.run(token)