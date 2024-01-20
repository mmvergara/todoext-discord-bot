import os
from firebase_admin import credentials, firestore, initialize_app
from firebase.models import Project

# Initialize Firebase
service_key_path = os.path.join(os.path.dirname(__file__),"..", "firebase-credentials.json")
cred = credentials.Certificate(service_key_path)
initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

print("Firebase initialized")


def connect_user(discord_user_id: str, project_id: str):
    """Connect a discord user to a project"""
    user_ref = db.collection("discord_users").document(str(discord_user_id))
    user_ref.set({"project_id": project_id})
