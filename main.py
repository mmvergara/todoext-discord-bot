import os
import discord
from discord.ext import commands
from dotenv import load_dotenv,find_dotenv
bot = commands.Bot(command_prefix='td ',intents=discord.Intents.all())

@bot.event
async def on_ready():
  await bot.load_extension("commands.text-commands")
  print('Bot is ready!')


# Load the .env file
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Run the bot
bot.run(token=BOT_TOKEN)


