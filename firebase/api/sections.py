from firebase.firestore import db
from google.cloud.firestore import SERVER_TIMESTAMP
from helpers.generators import generate_section_id


def add_section(project_id: str, section_name: str):
    """Add a section to a project"""
    print("=====================================")
    print(f"Adding section {section_name} to project {project_id}")
    print("\n\n")
    generated_section_id = generate_section_id()
    project_ref = db.collection("projects").document(project_id)
    project_ref.update(
        {
            f"sections.{generated_section_id}": {
                "sectionName": section_name,
                "tasks": {},
                "createdAt": SERVER_TIMESTAMP,
            }
        }
    )


def delete_section(project_id: str, section_id: str):
    """Delete a section from a project"""
    print("=====================================")
    print(f"Deleting section {section_id} from project {project_id}")
    print("\n\n")
    project_ref = db.collection("projects").document(project_id)
    project_ref.update(
        {
            f"sections.{section_id}": db.DELETE_FIELD,
        }
    )


# Tests
