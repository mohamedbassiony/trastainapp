from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        project_dir = os.path.join(self.files_dir, project_id)

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir


    def get_destination_path(self, project_id: str):
        destination_dir = os.path.join(self.destination_dir, project_id)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        return destination_dir