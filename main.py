import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv, find_dotenv
from firebase import connect_user

test_guild = 910166218181345320
bot = commands.Bot(command_prefix="td ", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.load_extension("cogs.text_commands")
    try:
        # await bot.tree.sync(guild=discord.Object(id=test_guild))
        print("Synced")
    except Exception as e:
        print(e)
    print("Bot is ready!")


@bot.tree.command(
    name="ping",
    description="Shows the bot latency",
    guild=discord.Object(id=test_guild),
)
async def ping(interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")


# take 1 argument, a project name
@bot.tree.command(
    name="connect",
    description="Connect to a project",
    guild=discord.Object(id=test_guild),
)
@app_commands.describe(project_key="Project Key")
async def connect(interaction, project_key: str):
    try:
        await connect_user(interaction.user.id, project_key)
        await interaction.response.send_message(f"Connected to {project_key}")
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Error Connecting to {project_key}")


# Load the .env file
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Run the bot
bot.run(token=BOT_TOKEN)