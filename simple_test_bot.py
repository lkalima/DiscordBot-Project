import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Enable intents, including message content
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot with intents
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
bot.run(TOKEN)
