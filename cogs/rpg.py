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

    @commands.command(name='total', help='Sum up any number of n-sided dice rolls.')
    async def total(self,ctx,dice:str):
        dice = dice.split('d')
        number_dice = int(dice[0])
        sides = int(dice[1])
        dicerolls = [
            random.choice(range(1, sides + 1))
            for _ in range(number_dice)
        ]
        await ctx.reply('You rolled '  + str(number_dice) +'d' + str(sides) + '. Your results:\n' + str(sum(dicerolls)))


    @commands.command(name='rollstats', help='Rolls stats for Dungeons and Dragons characters. Try -dl or -og for different methods')
    async def rollstats(self,ctx,args:str):
        if '-dl' in args:
            rolls = [[random.choice(range(1, 7)) for _ in range(4)] for _ in range(6)]
            for sublist in rolls:
                sublist.remove(min(sublist))
            result_string = f"Your stat-rolls are:\n"
            for i in range(len(rolls)):
                result_string += f"{str(i+1)}. [{', '.join([str(n) for n in rolls[i]])}] = {str(sum(rolls[i]))}\n"
            await ctx.reply(result_string)
            return
        if '-og' in args:
            rolls = [[random.choice(range(1, 7)) for _ in range(3)] for _ in range(6)]
            result_string = f"Your stat-rolls are:\n"
            for i in range(len(rolls)):
                result_string += f"{str(i+1)}. [{', '.join([str(n) for n in rolls[i]])}] = {str(sum(rolls[i]))}\n"
            await ctx.reply(result_string)
            return
        # TODO : min 8 for reroll if a stat is 7 or lower
        # TODO : min X for reroll if a stat is X or lower

def setup(bot):
    bot.add_cog(RPG(bot))