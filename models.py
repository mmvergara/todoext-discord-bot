from typing import Dict
from datetime import datetime


class Project:
    def __init__(
        self,
        project_id: str,
        project_name: str,
        project_key: str,
        owner_id: str,
        collaborators: Dict[str, str],
        created_at: datetime,
        sections: Dict[str, "Section"],
    ):
        self.project_id = project_id
        self.project_name = project_name
        self.project_key = project_key
        self.owner_id = owner_id
        self.collaborators = collaborators
        self.created_at = created_at
        self.sections = sections


class Section:
    def __init__(
        self, section_name: str, tasks: Dict[str, "Task"], created_at: datetime
    ):
        self.section_name = section_name
        self.tasks = tasks
        self.created_at = created_at


class Task:
    def __init__(self, task_name: str, created_at: datetime):
        self.task_name = task_name
        self.created_at = created_at
