import discord
from discord.ext import commands

class HeldenAufPapier(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_in_guild():
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == heldenaufpapier_id
        return commands.check(predicate)

    ##### Commands specific to the HeldenAufPapier community #####

    #Add role 'imp' to newly joined users
    @commands.Cog.listener()
    @is_in_guild()
    async def on_member_join(self, member):
        try:
            role_id_imp = '694872569073107114' # Role-id of role 'imp'
            imp_role = member.guild.get_role(int(role_id_imp))
            await member.add_roles(imp_role)
        except discord.Forbidden:
            print(f'Cannot add role {imp_role} to user {member.name}.')
        except discord.NotFound:
            print(f'Role {imp_role} not found.')

    @commands.command(name='cassandra', help='Stream-specific command concerning a characters untimely death')
    @is_in_guild()
    async def cassandra(self, ctx):
        await ctx.send('In der Session vom 15.04.2020 wurde Cassandra, @davemithut\'s erster Spielercharakter in der "Descent Into Avernus" Kampagne, durch eine herabfallende Decke erschlagen (weil Simon eins seiner Features vergessen hat).')

#ServerID of the HeldenAufPapier-Server
heldenaufpapier_id = 694869619730546768

def setup(bot):
    bot.add_cog(HeldenAufPapier(bot))