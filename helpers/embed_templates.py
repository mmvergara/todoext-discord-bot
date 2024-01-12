from firebase.models import Project
from discord import Embed


def create_project_embed(project: Project) -> Embed:
    embed = Embed(
        title=f"Project: {project.projectName}",
        description=f"----------------------------",
        color=0xDD7C36,
    )

    for _, section in project.sections.items():
        section_str = ""
        for _, task in section["tasks"].items():
            section_str += f"{task['taskName']}\n"
        section_str += "---------------------------- \n"
        embed.add_field(name=section["sectionName"], value=section_str, inline=False)

    return embed


def error_embed(error_message: str):
    embed = Embed(
        title="Error",
        description=f"{error_message}",
        color=0xF73939,
    )
    return embed
