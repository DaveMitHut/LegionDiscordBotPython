# legion.py
import os
import discord
import json
import re
import random
import requests
from discord.ext import commands
#from dotenv import load_dotenv

#Load Token from local file (ONLY FOR DEVELOPMENT)
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.environ.get('LEGION_TOKEN', 3)

bot = commands.Bot(command_prefix='!')

@bot.command(name='cassandra', help='Stream-specific command concerning a characters untimely death')
async def cassandra(ctx):
    await ctx.send('In der Session vom 15.04.2020 wurde Cassandra, @davemithut\'s erster Spielercharakter in der "Descent Into Avernus" Kampagne, durch eine herabfallende Decke erschlagen (weil Simon eins seiner Features vergessen hat).')

@bot.command(name='roll', help='Roll any number of n-sided dice with a + or - modifier')
async def roll(ctx, dice:str):
    dice = dice.split('d')
    number_dice = int(dice[0])
    if ('+' in dice[1]):
        sides_mod = dice[1].split('+')
        sides = int(sides_mod[0])
        mod = int(sides_mod[1])
        dicerolls = [
            str(random.choice(range(1 + mod, sides + mod + 1)))
            for _ in range(number_dice)
        ]
        await ctx.reply('You rolled '  + str(number_dice) +'d' + str(sides) + '+' + str(mod) + '. Your results:\n' + '\n'.join(dicerolls)) 
    elif ('-' in dice[1]):
        sides_mod = dice[1].split('-')
        sides = int(sides_mod[0])
        mod = int(sides_mod[1])
        dicerolls = [
            str(random.choice(range(1 - mod, sides - mod + 1)))
            for _ in range(number_dice)
        ]
        await ctx.reply('You rolled '  + str(number_dice) +'d' + str(sides) + '-' + str(mod) + '. Your results:\n' + '\n'.join(dicerolls))
    else:
        sides = int(dice[1])
        dicerolls = [
            str(random.choice(range(1, sides + 1)))
            for _ in range(number_dice)
        ]
        await ctx.reply('You rolled '  + str(number_dice) +'d' + str(sides) + '. Your results:\n' + '\n'.join(dicerolls))

@bot.command(name='card', help='Fetch any MtG card\'s image')
async def card_image(ctx, cardname: str):
    data = fetchCardFromScryfall(cardname)
    await ctx.send(data['image_uris']['normal'])

@bot.command(name='legality', help='Fetch format legality for any MtG card')
async def card_legality(ctx, cardname: str):
    data = fetchCardFromScryfall(cardname)
    await ctx.send('Commander: ' + data['legalities']['commander'] + '\nStandard: ' + data['legalities']['standard'] + '\nModern: ' + data['legalities']['modern'])

@bot.command(name='rulings', help='Fetch rulings for any MtG card')
async def card_legality(ctx, cardname: str):
    data = fetchCardFromScryfall(cardname)
    rulings_request_url = 'https://api.scryfall.com/cards/' + data['id'] + '/rulings'
    rulings_response = requests.get(rulings_request_url)
    rulings_data = rulings_response.json()
    response = ''
    for i in range(0, len(rulings_data['data'])):
        response += '\n' + 'From: ' + rulings_data['data'][i]['source'] + '\n' + rulings_data['data'][i]['comment']
    await ctx.send(response)

@bot.event
async def on_member_join(member):
    greeting = 'Hi ' + member.name + ', willkommen auf dem ' + member.guild.name + ' Discord Server!\nHi ' + member.name + ', welcome to the ' + member.guild.name + ' discord server!'
    if guild.system_channel is not None:
        await guild.system_channel.send(greeting)
    else:
        await member.send(greeting)
    try:
        #Add role 'imp' to newly joined users -- Only works on HeldenAufPapier Server
        role_id = '694872569073107114' # Role-id of role 'imp'
        role = member.guild.get_role(int(role_id))
        await member.add_roles(role)
    except discord.Forbidden:
        printf('Cannot add role {role} to user {member.name}.')
    except discord.NotFound:
        printf('Role {role} not found.')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

def fetchCardFromScryfall(cardname: str):
    request_url = 'https://api.scryfall.com/cards/named?fuzzy='
    cardname = cardname.split(' ')
    for i in range(0, len(cardname)):
        if i == 0:
            request_url += cardname[i]
        else:
            request_url += '+' + cardname[i]
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as errh:
        print('HTTP Error: ', errh)
    except requests.exceptions.ConnectionError as errc:
        print('Connection Error: ', errc)
    except requests.exceptions.Timeout as errt:
        print('Timeout Error: ', errt)
    except requests.exceptions.RequestException as err:
        print('Something went wrong: ', err)

bot.run(TOKEN)
