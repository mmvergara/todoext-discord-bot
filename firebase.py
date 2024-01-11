import os
from firebase_admin import credentials, firestore, initialize_app
from models import Project

# Initialize Firebase
service_key_path = os.path.join(os.path.dirname(__file__), "firebase-credentials.json")
cred = credentials.Certificate(service_key_path)
initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()


def connect_user(discord_user_id: str, project_id: str):
    """Connect a discord user to a project"""
    user_ref = db.collection("discord_users").document(str(discord_user_id))
    user_ref.set({"project_id": project_id})


def get_project_id(discord_user_id: str):
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
            project_id=doc.id,
            project_name=project_dict["projectName"],
            project_key=project_dict["projectKey"],
            owner_id=project_dict["ownerId"],
            collaborators=project_dict["collaborators"],
            created_at=project_dict["createdAt"],
            sections=project_dict["sections"],
        )
        return project

    return None


print(get_project("qweqwe89c386f858g5geeidk5j"))
