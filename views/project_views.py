from utils.print_table import table_of_options, projects_table
from utils.colors import *

def create_project(project_controller, user_input):
    title = user_input.get_valid_title(f"{Colors.RESET}Enter project title: {Colors.BLUE}")
    description = user_input.get_valid_description(f"{Colors.RESET}Enter project description: {Colors.BLUE}")
    target_money = user_input.get_valid_target_money(f"{Colors.RESET}Enter project target money: {Colors.BLUE}")
    start_date = user_input.get_valid_date(f"{Colors.RESET}Enter project start date: {Colors.BLUE}")
    end_date = user_input.get_valid_date(f"{Colors.RESET}Enter project end date: {Colors.BLUE}", start_date)

    project_controller.create_project(title, description, target_money, start_date, end_date)

    print_colored("\nProject created successfully\n", Colors.GREEN)

def view_projects(project_controller, prompt=True):

    projects = project_controller.get_projects()

    if len(projects) == 0:
        print_colored("\nThere are no projects to view\n", Colors.RED)
        return False

    projects_table(projects)

    if prompt:
        input("press any key to continue...")
        print()
    
    return True

def edit_project(project_controller, user_input):
    status = view_projects(project_controller, False)
    if status:
        while True:
            project_id = input("Select a project id you want to update or n to exit: ")
            if project_id == "n":
                break
            status, message = project_controller.is_owner(project_id)
            if status:
                project = project_controller.get_project_by_id(project_id)
                is_updated = False
                while True:
                    choice = table_of_options("Which field you want to update", 
                                            "Title", 
                                            "Description", 
                                            "Target money", 
                                            "Start date", 
                                            "End date", 
                                            "Exit")
                    if choice == "1":
                        title = user_input.get_valid_title(f"{Colors.RESET}Enter project title: {Colors.BLUE}")
                        project.title = title
                    elif choice == "2":
                        description = user_input.get_valid_description(f"{Colors.RESET}Enter project description: {Colors.BLUE}")
                        project.description = description
                    elif choice == "3":
                        target_money = user_input.get_valid_target_money(f"{Colors.RESET}Enter project target money: {Colors.BLUE}")
                        project.total_target = target_money
                    elif choice == "4":
                        start_date = user_input.get_valid_date(f"{Colors.RESET}Enter project start date: {Colors.BLUE}", not_after=project.end_date)
                        project.start_date = start_date
                    elif choice == "5":
                        end_date = user_input.get_valid_date(f"{Colors.RESET}Enter project end date: {Colors.BLUE}", not_before=project.start_date)
                        project.end_date = end_date
                    elif choice == "6":
                        break
                    else:
                        print_colored("\nInvalid option\n", Colors.RED)
                        continue

                    is_updated = True
                    c = input(f"\n{Colors.RESET}Do you want to continue editing this project? (y/n): {Colors.BLUE}")
                    print(Colors.RESET)
                    if c != 'y':
                        break

                if is_updated:
                    project_controller.update_project(project)
                    print_colored("\nProject updated successfully\n", Colors.GREEN)
                else:
                    print_colored("\nProject not updated\n", Colors.RED)
                break
            else:
                print_colored(f"\nError: { message }\n", Colors.RED)
        

def delete_project(project_controller):
    status = view_projects(project_controller, False)
    if status:
        while True:
            project_id = input("Select a project id you want to delete or n not exit: ")
            if project_id == "n":
                break
            status, message = project_controller.is_owner(project_id)
            if status:
                project_controller.delete_project(project_id)
                print_colored("\nProject deleted successfully\n", Colors.GREEN)
                break
            else:
                print_colored(f"\nError: { message }\n", Colors.RED)

