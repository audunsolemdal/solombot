import discord
import random
from discord.ext import commands
from appsettings import SettingsParser

parser  = SettingsParser()
client = commands.Bot(command_prefix = '.')

parser.add_argument('--token', default='placeholderToken', env_var='TOKEN')
parser.add_argument('--url', default='placeholderUrl', env_var='url')
args = parser.parse_args()

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
    await context.send( 'g0mp2gether @ {args.url}')

@client.command(aliases=['8ball', 'g0mpball'])
async def _8ball(context):
    responses = [
        'Jepp',
        '100%'
    ]
    await context.send( random.choice(responses) )

client.run(args.token)