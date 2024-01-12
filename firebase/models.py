from typing import Dict
from datetime import datetime


class Project:
    def __init__(
        self,
        projectId: str,
        projectName: str,
        projectKey: str,
        ownerId: str,
        collaborators: Dict[str, str],
        createdAt: datetime,
        sections: Dict[str, "Section"],
    ):
        self.projectId = projectId
        self.projectName = projectName
        self.projectKey = projectKey
        self.ownerId = ownerId
        self.collaborators = collaborators
        self.createdAt = createdAt
        self.sections = sections


class Section:
    def __init__(
        self, sectionName: str, tasks: Dict[str, "Task"], createdAt: datetime
    ):
        self.sectionName = sectionName
        self.tasks = tasks
        self.createdAt = createdAt


class Task:
    def __init__(self, taskName: str, createdAt: datetime):
        self.taskName = taskName
        self.createdAt = createdAt
