from firebase.models import Project
from firebase.firestore import db


def get_project_key_by_discord_user_id(discord_user_id: str):
    """Get the project id for a discord user"""
    user_ref = db.collection("discord_users").document(discord_user_id)
    doc = user_ref.get()
    if doc.exists:
        return doc.to_dict()["project_id"]
    else:
        return None


def get_project_id_by_project_key(project_key: str):
    """Get the project id for a project key"""
    print("=====================================")
    print(f"Getting project id for project key {project_key}")
    print("\n\n")
    project_ref = db.collection("projects").where("projectKey", "==", project_key)
    docs = project_ref.stream()
    for doc in docs:
        return doc.id
    return None


def get_project(project_key: str) -> Project:
    """Get a project that matches the project_key"""
    docs = db.collection("projects").where("projectKey", "==", project_key).stream()

    for doc in docs:
        project_dict = doc.to_dict()
        project = Project(
            projectId=doc.id,
            projectName=project_dict["projectName"],
            projectKey=project_dict["projectKey"],
            ownerId=project_dict["ownerId"],
            collaborators=project_dict["collaborators"],
            createdAt=project_dict["createdAt"],
            sections=project_dict["sections"],
        )

        # Sort tasks in each section by createdAt
        for section in project.sections.values():
            sorted_tasks = sorted(
                section["tasks"].items(), key=lambda x: x[1]["createdAt"]
            )
            section["tasks"] = dict(sorted_tasks)

        # Sort sections by createdAt
        sorted_sections = sorted(
            project.sections.items(), key=lambda x: x[1]["createdAt"]
        )
        project.sections = dict(sorted_sections)

        return project

    return None
