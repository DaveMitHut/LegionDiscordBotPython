import os
import discord
from discord.ext import commands
#from dotenv import load_dotenv

#Load token from local file (ONLY FOR DEVELOPMENT)
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

#Load token from Heroku
TOKEN = os.environ.get('LEGION_TOKEN', 3)

initial_extensions = ['cogs.general',
                      'cogs.rpg',
                      'cogs.mtg',
                      'cogs.heldenaufpapier']

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#Get response when bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN, bot=True, reconnect=True)