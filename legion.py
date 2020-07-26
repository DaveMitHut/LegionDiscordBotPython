import json
import random
import discord
import requests

client = discord.Client()

existing_commands = ['!commands', '!card', '!cards', '!legality', '!legalities', '!legal', '!rulings', '!ruling', '!roll', '!cassandra']
mtg_commands = ['!card', '!cards', '!legality', '!legalities', '!legal', '!rulings', '!ruling']

@client.event
async def on_message(msg):
    if msg.content.startswith('!'):
        message_content = msg.content.split(' ')
        if message_content[0] not in existing_commands:
            await msg.channel.send('Looks like you have a typo in your command.\nType !commands to get a list of all available commands.')
        elif message_content[0] in existing_commands:
            # Display list of commands
            if msg.content.startswith('!commands'):
                await msg.channel.send('Here is a list of commands you can use:\n!card cardname -> displays card for a given cardname\n\n!legality cardname -> displays a cards legalities for Commander, Standard & Modern formats\n\n!rulings cardname -> displays existing rulings for a card\n\n!roll xdx -> rolls the specified number of dice')

            # Stream-specific commands
            elif msg.content.startswith('!cassandra'):
                await msg.channel.send('In der Session vom 15.04.2020 wurde Cassandra, @davemithut erster Spielercharakter in dieser Kampagne, durch eine herabfallende Decke erschlagen (weil Simon sein Feature vergessen hat).')
            
            # Roll randomly generated specified dice
            elif msg.content.startswith('!roll'):
                content = msg.content.split(' ')
                dice = content[1].split('d')
                number_dice = int(dice[0])
                sides = int(dice[1])
                await msg.channel.send('Rolling ' + content[1])
                for i in range(number_dice):
                    rand_roll = random.randrange(1, sides + 1)
                    await msg.channel.send('\nRoll ' + str(i + 1) + ': ' + str(rand_roll))

            # Call scryfall API for commands !ruling, !legality, !card
            if message_content[0] in mtg_commands:
                card_name = msg.content.split(' ')
                req = 'https://api.scryfall.com/cards/named?fuzzy='

                for i in range(1, len(card_name)):
                    if i == 1:
                        req += card_name[i]
                    else:
                        req += '+' + card_name[i]

                response = requests.get(req)
                data = response.json()

                if msg.content.startswith('!card') or msg.content.startswith('!cards'):
                    await msg.channel.send(data['image_uris']['normal'])

                elif msg.content.startswith('!legality') or msg.content.startswith('legalities') or msg.content.startswith('legal'):
                    await msg.channel.send('Commander: ' + data['legalities']['commander'] + '\nStandard: ' + data['legalities']['standard'] + '\nModern: ' + data['legalities']['modern'])
        
                elif msg.content.startswith('!rulings') or msg.content.startswith('ruling'):
                    rulings_req = 'https://api.scryfall.com/cards/' + data['id'] + '/rulings'
                    rulings_response = requests.get(rulings_req)
                    rulings_data = rulings_response.json()
                    for i in range(0, len(rulings_data['data'])):
                        await msg.channel.send('\n' + 'From: ' + rulings_data['data'][i]['source'] + '\n' + rulings_data['data'][i]['comment'])

@client.event
async def on_member_join(member):
    await member.send('Willkommen auf unserem Server! Um zu sehen, wozu diese Entität fähig ist, schreibe "!commands" in einen der Chaträume.')
    await member.send('Welcome to our Server! If you want to see what this entity is capable of, type "!commands" in the main chatroom.')
    try:
        #Add role 'imp' to newly joined users
        role_id = '694872569073107114' # Role-id of role 'imp'
        role = member.guild.get_role(int(role_id))
        await member.add_roles(role)
    except discord.Forbidden:
        print('Cannot add roles.')
    except discord.NotFound:
        print('Role not found.')

# Missings:
# Scryfall API functions:
    # Handle error codes

# Twitch API functions:
    # Message when stream goes live
    # Message when stream finished

client.run(LEGION_TOKEN)