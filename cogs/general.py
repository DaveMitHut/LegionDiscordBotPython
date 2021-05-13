from discord.ext import commands
import random

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##### General commands #####

    @commands.Cog.listener()
    async def on_member_join(self, member):
        greeting = 'Hi ' + member.name + ', willkommen auf dem ' + member.guild.name + ' Discord Server!\nHi ' + member.name + ', welcome to the ' + member.guild.name + ' discord server!'
        if member.guild.system_channel is not None:
            await member.guild.system_channel.send(greeting)
        else:
            await member.send(greeting)

    @commands.command(name='coinflip', help='Flip a coin')
    async def coinflip(self, ctx):
        coin = random.randint(0, 1)
        if (coin == 0):
            await ctx.reply('Heads')
        else:
            await ctx.reply('Tails')

def setup(bot):
    bot.add_cog(General(bot))