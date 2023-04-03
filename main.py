from controllers.auth_controller import AuthController
from controllers.project_controller import ProjectController
from utils.get_valid_input import ValidInput
from utils.print_table import table_of_options, projects_table
from views import auth_views ,project_views
from utils.colors import *

user_input = ValidInput()

def welcome_banner():
    banner = f"""{Colors.GREEN}   ______                           __           
  / ____/_____ ____  _      __ ____/ /           
 / /    / ___// __ \| | /| / // __  /            
/ /___ / /   / /_/ /| |/ |/ // /_/ /             
\____//_/    \____/ |__/|__/ \__,_/              
                                                 
    ____                   __ _                  
   / __/__  __ ____   ____/ /(_)____   ____ _    
  / /_ / / / // __ \ / __  // // __ \ / __ `/    
 / __// /_/ // / / // /_/ // // / / // /_/ /     
/_/   \__,_//_/ /_/ \__,_//_//_/ /_/ \__, /      
                                    /____/       
                                                 
  ____ _ ____   ____                             
 / __ `// __ \ / __ \                            
/ /_/ // /_/ // /_/ /                            
\__,_// .___// .___/                             
     /_/    /_/                                  
     {Colors.RESET}\n\n""" + f"""
     {Colors.YELLOW}By: {Colors.MAGENTA}Khaled Gad{Colors.RESET}\n\n"""
    
    
    print(banner)

def project_menu(logged_in_user):
    project_controller = ProjectController(logged_in_user)
    while True:
        choice = table_of_options("Please choose an option", "Create Project", "View Projects", "Edit Project", "Delete Project", "Logout", "Exit")
        if choice == "1":
            project_views.create_project(project_controller, user_input)
        elif choice == "2":
            project_views.view_projects(project_controller)
        elif choice == "3":
            project_views.edit_project(project_controller, user_input)
        elif choice == "4":
            project_views.delete_project(project_controller, user_input)
        elif choice == "5":
            print_colored("\nLogged out successfully\n", Colors.GREEN)
            break
        elif choice == "6":
            auth_views.exit_app()
        else:
            print_colored("\nInvalid choice, please try again\n", Colors.RED)

def main_menu():
    auth_controller = AuthController()
    while True:
        choice = table_of_options("Please choose an option", "Login", "Register", "Exit")
        if choice == "1":
            user = auth_views.login(auth_controller, user_input)
            if user:
                project_menu(user)
        elif choice == "2":
            auth_views.register(auth_controller, user_input)
        elif choice == "3":
            auth_views.exit_app()
        else:
            print_colored("\nInvalid choice, please try again\n", Colors.RED)

if __name__ == "__main__":
    welcome_banner()
    main_menu()