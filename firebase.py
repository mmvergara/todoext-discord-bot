import os 
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase
service_key_path = os.path.join(os.path.dirname(__file__),"firebase-credentials.json")
cred = credentials.Certificate(service_key_path)
initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()




def connect_user(discord_user_id:str, project_id:str):
    """Connect a discord user to a project"""
    user_ref = db.collection(u'discord_users').document(discord_user_id)
    user_ref.set({
        u'project_id': project_id
    })

def get_project_id(discord_user_id:str):
    """Get the project id for a discord user"""
    user_ref = db.collection(u'discord_users').document(discord_user_id)
    doc = user_ref.get()
    if doc.exists:
        return doc.to_dict()['project_id']
    else:
        return None


def get_project(project_id:str):
    """Get a project by id"""
    project_ref = db.collection(u'projects').document(project_id)
    doc = project_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def get_project_sections(project_id:str):
    """Get the sections for a project"""
    sections_ref = db.collection(u'projects').document(project_id).collection(u'sections')
    docs = sections_ref.stream()
    return [doc.to_dict() for doc in docs]