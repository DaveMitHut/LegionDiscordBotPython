from discord.ext import commands
import random

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

def setup(bot):
    bot.add_cog(RPG(bot))