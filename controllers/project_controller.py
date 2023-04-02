from models.project import Project

class ProjectController:
    def __init__(self, logged_in_user):
        self.user = logged_in_user

    def create_project(self, title,  description, total_target, start_date, end_date):
        new_project = Project(title, description, total_target, start_date, end_date)
        new_project.owner_id = self.user.id
        new_project.save()
        return new_project
    
    def get_projects(self):
        projects = Project.get_projects()
        return projects
    
    def get_project_by_id(self, id):
        project = Project.find_by_id(id)
        return project
    

        