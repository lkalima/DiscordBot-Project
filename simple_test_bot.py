import discord
from discord.ext import commands

# Set up bot with a command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! How can I assist you?")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
bot.run("YOUR_BOT_TOKEN_HERE")
