import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv, find_dotenv
from firebase.firestore import connect_user
from firebase.api.sections import add_section
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
async def ping_cmd(interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")


# Connect to a project
@bot.tree.command(
    name="connect",
    description="Connect to a project",
)
@app_commands.describe(project_key="Project Key")
async def connect_cmd(interaction, project_key: str):
    try:
        connect_user(interaction.user.id, project_key)
        await interaction.response.send_message(f"Connected to {project_key}")
    except Exception as e:
        print(e)
        await interaction.response.send_message(f"Error Connecting to {project_key}")


# Add Section
@bot.tree.command(
    name="add-section",
    description="Add a section",
)
@app_commands.describe(section_name="New Section Name")
async def add_section_cmd(interaction, section_name: str):
    await interaction.response.send_message(f"Added {section_name}")


# Add Task
@bot.tree.command(
    name="add-task",
    description="Add a task",
)
@app_commands.describe(section_id="Section ID")
@app_commands.describe(task_name="New Task Name")
async def add_task_cmd(interaction, section_id: str, task_name: str):
    await interaction.response.send_message(f"Added {task_name} to {section_id}")


# Delete Section
@bot.tree.command(
    name="delete-section",
    description="Delete a section",
)
@app_commands.describe(section_id="Section ID")
async def delete_section_cmd(interaction, section_id: str):
    await interaction.response.send_message(f"Deleted {section_id}")


# Delete Task
@bot.tree.command(
    name="delete-task",
    description="Delete a task",
)
@app_commands.describe(section_id="Section ID")
@app_commands.describe(task_id="Task Name")
async def delete_task_cmd(interaction, section_id: str, task_id: str):
    await interaction.response.send_message(f"Deleted {task_id} from {section_id}")


# Load the .env file
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Run the bot
add_section("N0eM8s8domhH1NEzSVvC", "TESTS SEE")
bot.run(token=BOT_TOKEN)
