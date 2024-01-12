from firebase.firestore import db
from google.cloud.firestore import SERVER_TIMESTAMP,DELETE_FIELD
from helpers.generators import generate_section_id


def add_section(project_id: str, section_name: str) -> bool:
    """Add a section to a project"""
    print(f"API: Adding section {section_name} to project {project_id}")
    generated_section_id = generate_section_id()
    try:
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
      return True
    except Exception as e:
      print(e)
      return False


def delete_section(project_id: str, section_id: str) -> bool:
    """Delete a section from a project"""
    print(f"API: Deleting section {section_id} from project {project_id}")
    try:
        project_ref = db.collection("projects").document(project_id)
        project_ref.update(
            {
                f"sections.{section_id}": DELETE_FIELD,
            }
        )
        return True
    except Exception as e:
        print(e)
        return False


# Tests
