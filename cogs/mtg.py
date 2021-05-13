from discord.ext import commands
import requests

class MtG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##### MtG-centered commands #####

    @commands.command(name='card', help='Fetch any MtG card\'s image')
    async def card_image(self, ctx, cardname: str):
        data = fetchCardFromScryfall(cardname)
        await ctx.send(data['image_uris']['normal'])

    @commands.command(name='legality', help='Fetch format legality for any MtG card')
    async def card_legality(self, ctx, cardname: str):
        data = fetchCardFromScryfall(cardname)
        await ctx.send('Commander: ' + data['legalities']['commander'] + '\nStandard: ' + data['legalities']['standard'] + '\nModern: ' + data['legalities']['modern'])

    @commands.command(name='rulings', help='Fetch rulings for any MtG card')
    async def card_rulings(self, ctx, cardname: str):
        data = fetchCardFromScryfall(cardname)
        rulings_request_url = 'https://api.scryfall.com/cards/' + data['id'] + '/rulings'
        rulings_response = requests.get(rulings_request_url)
        rulings_data = rulings_response.json()
        response = ''
        for i in range(0, len(rulings_data['data'])):
            response += '\n' + 'From: ' + rulings_data['data'][i]['source'] + '\n' + rulings_data['data'][i]['comment']
        await ctx.send(response)

##### General methods to be used by commands #####

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

def setup(bot):
    bot.add_cog(MtG(bot))