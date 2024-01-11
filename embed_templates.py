from models import Project
from discord import Embed


def create_project_embed(project: Project) -> Embed:
    embed = Embed(
        title=f"Project: {project.projectName}",
        description=f"-----------------",
        color=0x3498DB,
    )

    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.png")
    embed.thumbnail.width = 300
    embed.thumbnail.height = 300

    for _, section in project.sections.items():
        section_str = ""
        for _, task in section["tasks"].items():
            section_str += f"{task['taskName']}\n"
        section_str += "----------------- \n"
        embed.add_field(name=section["sectionName"], value=section_str, inline=False)

    return embed


def error_embed(error_message: str):
    embed = Embed(
        title=f"Error: {error_message}",
        color=0xF73939,
    )
    return embed
