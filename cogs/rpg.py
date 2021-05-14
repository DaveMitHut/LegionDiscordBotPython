from discord.ext import commands
import random

##### diceRoller - rollCommandParser #####

def __rolls(sides, count):
    return [random.choice(range(1, sides + 1)) for _ in range(0,count)]

def __rollCommandParser(dice:str):
    dice = dice.split('d')
    sides = 0
    count = 0
    mod = 0
    if len(dice) < 2 and dice[1] == '':
        return None
    try:
        count = int(dice[0])
    except:
        return None
        
    if ('+' in dice[1]):
        sides_mod = dice[1].split('+')
        sides = int(sides_mod[0])
        mod = int(sides_mod[1])
        return sides,count,mod

    if ('-' in dice[1]):
        sides_mod = dice[1].split('+')
        sides = int(sides_mod[0])
        mod = int(sides_mod[1])*-1
        return sides,count,mod

class RPG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##### RPG-centered commands #####

    @commands.command(name='roll', help='Roll any number of n-sided dice with a + or - modifier')
    async def roll(self, ctx, dice:str):
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
        await ctx.reply('Something went wrong!')

    @commands.command(name='total', help='Sum up any number of n-sided dice rolls with a + or - modifier')
    async def total(self,ctx,dice:str):
        await ctx.reply('TBD')

    @commands.command(name='rollstats', help='Rolls stats for Dungeons and Dragons characters. Try -dl or -og for different methods')
    async def rollstats(self,ctx,args:str):
        stats = []
        if '-og' in args:
            for _ in range(0,6):
                stats.append(str(sum(__rolls(6,3))))
        else:
            for _ in range(0,6):
                tempstat = __rolls(6,4)
                stats.append(str(sum(tempstat)-min(tempstat)))
        # TODO : min 8 for reroll if a stat is 7 or lower
        # TODO : min X for reroll if a stat is X or lower



def setup(bot):
    bot.add_cog(RPG(bot))