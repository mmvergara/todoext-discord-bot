from firebase.models import Project
from firebase.firebase import db


def get_project_key_by_discord_user_id(discord_user_id: str):
    """Get the project id for a discord user"""
    user_ref = db.collection("discord_users").document(discord_user_id)
    doc = user_ref.get()
    if doc.exists:
        return doc.to_dict()["project_id"]
    else:
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

        return project

    return None
