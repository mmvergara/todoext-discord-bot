from firebase.models import Project
from discord import Embed


def create_project_embed(project: Project) -> Embed:
    embed = Embed(
        title=f"{project.projectName}",
        description=f"----------------------------",
        color=0xDD7C36,
    )
    empty_sections = []
    for section_id, section in project.sections.items():
        # Skip empty sections
        if len(section["tasks"]) == 0:
            empty_sections.append([section["sectionName"], section_id])
            continue

        section_str = ""
        for _, task in section["tasks"].items():
            section_str += f"{task['taskName']}\n"
        section_str += "---------------------------- \n"
        embed.add_field(
            name=f"{section['sectionName']} - #{section_id}",
            value=section_str,
            inline=False,
        )

    # Add empty sections
    empty_sections_str = ""
    for section in empty_sections:
        empty_sections_str += f"{section[0]} - #{section[1]}\n"
    embed.add_field(
        name=f"Empty Sections",
        value=empty_sections_str,
        inline=False,
    )

    return embed


def error_embed(error_message: str):
    embed = Embed(
        description=f"{error_message}",
        color=0xF73939,
    )
    return embed
