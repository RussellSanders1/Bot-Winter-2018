import flask, os, discord
from discord.ext.commands import Bot
from flask import Flask

BOT_PREFIX = os.environ.get('prefix')
TOKEN = os.environ.get('TOKEN')
client = Bot(command_prefix=BOT_PREFIX)

app = Flask(__name__)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)