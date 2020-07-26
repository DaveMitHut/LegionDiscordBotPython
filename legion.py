import discord

client = discord.Client()

exisiting_commands = ['!commands', '!card', '!cards', '!legality', '!legalities', '!legal', '!rulings', '!ruling', '!dice', '!roll', '!cassandra']

@client.event
async def on_message(msg):
    if msg.content[0] not in exisiting_commands:
        await msg.channel.send('It looks like you have a typo in your command.\nType !commands to get a list of available commands.')
    elif msg.content[0] in existing_commands:
        if msg.content.startsWith('!commands'):
            msg.channel.send('Here is a list of commands you can use:\n!card cardname -> displays card for a given cardname\n\n' \
                    '!legality cardname -> displays a cards legalities for Standard, Modern & Commander\n\n' \
                    '!rulings cardname -> displays existing rulings for a card\n\n' \
                    '!role xdx -> rolls the specified number of dice for you.)

        if msg.content.startsWith('!cassandra'):
            msg.channel.send('In der Session vom 15.04.2020 wurde Cassandra, @davemithut erster Spielercharakter in dieser Kampagne, durch eine herabfallende Decke erschlagen (weil Simon sein Feature vergessen hat).'
        
        if msg.content.startsWith('!roll'):
            content = msg.content.split(" ")
            dice = content[1].split("d")
            sides = dice[1]
            msg.channel.send('Rolling ' + content[1])
            for var in range(dice[0]):
                rand = Math.floor(Math.random() * sides) + 1;
                msg.channel.send('\nRoll ' + (i+1) + ': ' + rand)

        #Scryfall API functions !ruling, !legality, !card
    


@client.event
async def on_member_join(member):
    member.send('Willkommen auf unserem Server! Um zu sehen, wozu diese Entität fähig ist, schreibe "!commands" in einen der Chaträume.')
    member.send('Welcome to our Server! If you want to see what this entity is capable of, type "!commands" in the main chatroom.')
    #Add role imp to joined users
    #role = get roles 
    #member.add_roles(role)

# Twitch API functions:
# Message on stream goes live
# Message on stream finished

# Legion Bot token environment variable
    