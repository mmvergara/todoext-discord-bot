from firebase.firestore import db
from google.cloud.firestore import SERVER_TIMESTAMP
from helpers.generators import generate_task_id


def add_task(project_id: str, section_id: str, task_name: str) -> bool:
    """Add a task to a section"""
    print(f"API: Adding task {task_name} to section {section_id}")
    try:
        project_ref = db.collection("projects").document(project_id)
        project_ref.update(
            {
                f"sections.{section_id}.tasks.{generate_task_id()}": {
                    "taskName": task_name,
                    "createdAt": SERVER_TIMESTAMP,
                }
            }
        )
        return True
    except Exception as e:
        print(e)
        return False
