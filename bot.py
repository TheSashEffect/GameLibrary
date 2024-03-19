import discord
import os
import subprocess
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents().all()
bot = commands.Bot(case_insensitive=True, command_prefix='?', intents=intents, activity=discord.Streaming(name="for the people who are watching", url='https://www.twitch.tv/the_sash_effect'), help_command = None)

@bot.event
async def on_ready():       
    print(f'{bot.user.name} has connected to Discord')

@bot.event
async def on_command_error(ctx, error):
    # Check if the error is a command-related error
    if isinstance(error, commands.CommandError):
        # Get the error message
        error_message = f"An error occurred: {type(error).__name__} - {str(error)}"

        # Get the error channel
        error_channel1 = bot.get_channel(1172493971298201642)
        error_channel2 = bot.get_channel(1172582080878747668)

        # Send the error message to the specified channel
        await error_channel1.send(error_message)
        await error_channel2.send(error_message)
        
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! ' + str(bot.latency) + 'ms')
    
@bot.command()
async def temp(ctx):
    if ctx.author.id in (726079395974086680,769525682039947314,):
        await ctx.send(subprocess.run(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip())
    else:
        await ctx.send(f"You don't have access to this command @{ctx.author.name}")    

        

bot.run(TOKEN)