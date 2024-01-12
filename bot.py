import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv, find_dotenv
from firebase.firebase import connect_user

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
)
async def ping(interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")


# Connect to a project
@bot.tree.command(
    name="connect",
    description="Connect to a project",
)
@app_commands.describe(project_key="Project Key")
async def connect(interaction, project_key: str):
    try:
        connect_user(interaction.user.id, project_key)
        await interaction.response.send_message(f"Connected to {project_key}")
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Error Connecting to {project_key}")

# Add Task
@bot.tree.command(
    name="add-task",
    description="Add a task",
)
@app_commands.describe(section_name="Section Name")
@app_commands.describe(task_name="Task Name")
async def add_task(interaction, section_name: str, task_name: str):
    await interaction.response.send_message(f"Added {task_name} to {section_name}")


# Load the .env file
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Run the bot
bot.run(token=BOT_TOKEN)
