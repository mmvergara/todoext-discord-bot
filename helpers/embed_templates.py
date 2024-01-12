from firebase.models import Project
from discord import Embed


def create_project_embed(project: Project) -> Embed:
    embed = Embed(
        title=f"{project.projectName}",
        description=f"----------------------------",
        color=0xDD7C36,
    )
    # Sort sections by createdAt
    sorted_sections = sorted(project.sections.items(), key=lambda x: x[1]["createdAt"])

    for section_id, section in sorted_sections:
        if len(section["tasks"]) == 0:
            continue

        # Sort tasks by createdAt
        sorted_tasks = sorted(section["tasks"].items(), key=lambda x: x[1]["createdAt"])
        section_str = ""
        for _, task in sorted_tasks:
            section_str += f"{task['taskName']}\n"
        section_str += "---------------------------- \n"
        embed.add_field(name=f"{section['sectionName']} | {section_id}", value=section_str, inline=False)

    return embed


def error_embed(error_message: str):
    embed = Embed(
        title="Error",
        description=f"{error_message}",
        color=0xF73939,
    )
    return embed
