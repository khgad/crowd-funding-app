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
    
    def is_owner(self, project_id):
        project = Project.find_by_id(project_id)
        if project == None:
            return (False, "Project not found, Please enter a valid project id.")
        if project.owner_id != self.user.id:
            return (False, "You are not the owner of this project.")
        return (True, "You are the owner of this project.")

    def update_project(self, new_project):
        new_project.update()
        return (True, "Project updated successfully")
    
    def delete_project(self, project_id):
        project = Project.find_by_id(project_id)
        project.delete()
        return (True, "Project deleted successfully")

    

        