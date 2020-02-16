import discord
import random
from discord.ext import commands
import os

os.environ['TOKEN'] = "placeholder"
os.environ['URL'] = "placeholder"

token = os.environ['TOKEN']
url = os.environ['URL']

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


@client.command(aliases=['watch', 'w2g'])
async def _w2g(context):
    await context.send( 'g0mp2gether @ {url}')

@client.command(aliases=['8ball', 'g0mpball'])
async def _8ball(context):
    responses = [
        'Jepp',
        '100%'
    ]
    await context.send( random.choice(responses) )

client.run(token)