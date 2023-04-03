from controllers.auth_controller import AuthController
from controllers.project_controller import ProjectController
from utils.get_valid_input import ValidInput
from utils.print_table import table_of_options, projects_table


user_input = ValidInput()
class Colors:
    RESET = "\033[0;0m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"

def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")

def project_menu(logged_in_user):

    project_controller = ProjectController(logged_in_user)

    while True:
        choice = table_of_options("Please choose an option", "Create Project", "View Projects", "Edit Project", "Delete Project", "Logout", "Exit")

        if choice == "1":

            title = user_input.get_valid_title(f"{Colors.RESET}Enter project title: {Colors.BLUE}")
            description = user_input.get_valid_description(f"{Colors.RESET}Enter project description: {Colors.BLUE}")
            target_money = user_input.get_valid_target_money(f"{Colors.RESET}Enter project target money: {Colors.BLUE}")
            start_date = user_input.get_valid_date(f"{Colors.RESET}Enter project start date: {Colors.BLUE}")
            end_date = user_input.get_valid_date(f"{Colors.RESET}Enter project end date: {Colors.BLUE}", start_date)

            project_controller.create_project(title, description, target_money, start_date, end_date)

            print_colored("\nProject created successfully\n", Colors.GREEN)

        elif choice == "2":
            projects = project_controller.get_projects()
            if len(projects) == 0:
                print_colored("\nThere are no projects to view\n", Colors.RED)
            projects_table(projects)
            input("press any key to continue...")
            print()

        elif choice == "3":
            projects = project_controller.get_projects()
            if len(projects) == 0:
                print_colored("\nThere are no projects to update\n", Colors.RED)
            else:
                projects_table(projects)
                while True:
                    project_id = input("Select a project id you want to update: ")
                    # print("project_id: " + project_id)
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

        elif choice == "4":
            projects = project_controller.get_projects()
            if len(projects) == 0:
                print_colored("\nThere are no projects to delete\n", Colors.RED)
            else:
                projects_table(projects)
                while True:
                    project_id = input("Select a project id you want to delete: ")
                    status, message = project_controller.is_owner(project_id)
                    if status:
                        project_controller.delete_project(project_id)
                        print_colored("\nProject deleted successfully\n", Colors.GREEN)
                        break
                    else:
                        print_colored(f"\nError: { message }\n", Colors.RED)

        elif choice == "5":
            print_colored("\nLogged out successfully\n", Colors.GREEN)
            break

        elif choice == "6":
            print_colored("\nThank you for using Crowd-Funding App\n", Colors.GREEN)
            print_colored("Goodbye ^_^\n", Colors.CYAN)
            exit()

        else:
            print_colored("\nInvalid option\n", Colors.RED)

def main_menu():
    
    auth_controller = AuthController()

    print_colored("\nWelcome to the Crowd-Funding App\n", Colors.MAGENTA)

    while True:
        choice = table_of_options("Please choose an option", "Login", "Register", "Exit")

        if choice == "1":
            
            email = user_input.get_valid_email(f"{Colors.RESET}Enter your email: {Colors.BLUE}")
            password = user_input.get_valid_passwords(f"{Colors.RESET}Enter your password: {Colors.BLUE}")

            user = auth_controller.login(email, password)
            if user:
                print_colored("\nYou have successfully logged in\n", Colors.GREEN)
                project_menu(user)
            else:
                print_colored("\nInvalid email or password\n", Colors.RED)

        elif choice == "2":
            
            first_name = user_input.get_valid_name(f"{Colors.RESET}Enter your first name: {Colors.BLUE}")
            last_name = user_input.get_valid_name(f"{Colors.RESET}Enter your last name: {Colors.BLUE}")
            email = user_input.get_valid_email(f"{Colors.RESET}Enter your email: {Colors.BLUE}")
            password = user_input.get_valid_passwords(f"{Colors.RESET}Enter your password: {Colors.BLUE}")
            # confirm_password = user_input.get_valid_passwords("Confirm your password: {Colors.BLUE}")
            mobile_phone = user_input.get_valid_phone(f"{Colors.RESET}Enter your mobile phone number: {Colors.BLUE}")

            auth_controller.register(first_name, last_name, email, password, mobile_phone)

            print_colored("\nYou have successfully registered\n", Colors.GREEN)
        
        elif choice == "3":
            print_colored("\nThank you for using Crowd-Funding App\n", Colors.GREEN)
            print_colored("Goodbye ^_^\n", Colors.CYAN)
            exit()
        
        else:
            print_colored("\nInvalid choice, please try again\n", Colors.RED)
    

if __name__ == "__main__":
    main_menu()