import discord, os
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

BOT_PREFIX = os.environ.get('prefix')
TOKEN = os.environ.get('TOKEN')
statup_extensions = ["Music"]

bot = Bot(command_prefix=BOT_PREFIX)

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.event
async def on_ready():
    print("Bot online")
    print(TOKEN)
    print("--------------")


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")


@bot.command(pass_ccontext=True)
async def hello(ctx):
    await bot.say("Hi :smile:")


if __name__ == "__main__":
    for extension in statup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


bot.run(TOKEN)