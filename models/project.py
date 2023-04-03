import json
from utils.file_operations import *

class Project:

    projects_filename = 'data/projects.json'

    def __init__(self, title,  description, total_target, start_date, end_date, id = None, owner_id = None):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date

    def to_dect(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "total_target": self.total_target,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
    
    @classmethod
    def find_by_id(cls, id):
        projects = read_json_file(cls.projects_filename)
        for project in projects:
            if project['id'] == int(id):
                return cls(**project)
        return None
    
    @classmethod
    def get_projects(cls):
        projects = read_json_file(cls.projects_filename)
        return projects
    
    def save(self):
        projects = read_json_file(self.projects_filename)
        self.id = get_next_id(projects)
        projects.append(self.to_dect())
        write_json_file(self.projects_filename, projects)

    def update(self):
        projects = read_json_file(self.projects_filename)
        for project in projects:
            if project['id'] == self.id:
                project['title'] = self.title
                project['description'] = self.description
                project['total_target'] = self.total_target
                project['start_date'] = self.start_date
                project['end_date'] = self.end_date
        write_json_file(self.projects_filename, projects)

    def delete(self):
        projects = read_json_file(self.projects_filename)
        for project in projects:
            if project['id'] == self.id:
                projects.remove(project)
        write_json_file(self.projects_filename, projects)