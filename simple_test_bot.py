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
bot = commands.Bot(command_prefix="!", intents=intents,  application_id=1353371345248845875)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Slash command: /hello
@bot.tree.command(name="hello", description="Says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! How can I assist you?")

# Slash command: /ping
@bot.tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# Sync commands with Discord (this is required for slash commands)
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync the commands with Discord

    print(f'Logged in as {bot.user}')

# Run the bot
bot.run(TOKEN)
