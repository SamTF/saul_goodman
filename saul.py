###### IMPORTS        ############################################################
import rules_fetcher
import discord
from discord.ext import commands
from discord import app_commands

###### CONSTANTS        ##########################################################
TOKEN_FILE = '.saul_goodman.token'


###### DISCORD STUFF ############################################################
### Creating the bot!
class Saul(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='???', intents=intents)

    # on_ready event l think
    async def setup_hook(self) -> None:
        await self.tree.sync(guild=discord.Object(id=349267379991347200))
        print(f'Synced slash commands for {self.user} @ server 349267379991347200')
    
    # error handling
    async def on_command_error(self, ctx, error) -> None:
        await ctx.reply(error, ephemeral=True)

bot = Saul()


###### EVENTS        ##########################################################
# Runs this when the bot becomes online
@bot.event
async def on_ready():
    print("Better Call Saul!")
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game('Fighting for you!'))


@bot.hybrid_command(name='saul', with_app_command=True, description='Look up the ruling for an MTG ability 🤓')
@app_commands.guilds(discord.Object(id=349267379991347200)) # syncs the command only for this one server (way faster than global syncing)
async def saul(ctx, ability: str):
    ruling = rules_fetcher.fetch_rule(ability)
    await ctx.send(f"**{ability}:** *{ruling}*")


@discord.app_commands.command()
async def fruits(interaction: discord.Interaction, fruit: str):
    await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')




###### RUNNING THE BOT #################################################
if __name__ == "__main__":
    print("_____________SAUL GOODMAN INITIALISED_____________")
    with open(TOKEN_FILE, 'r') as f:
        token = f.read()
    
    bot.run(token)