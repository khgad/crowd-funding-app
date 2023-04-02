from controllers.auth_controller import AuthController
from controllers.project_controller import ProjectController
from utils.get_valid_input import ValidInput
from utils.print_table import table_of_options


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

            # title = input()
            # description = user_input.get_valid_description()
            # target_money = user_input.get_valid_target_money()
            # start_date = user_input.get_valid_start_date()
            # end_date = user_input.get_valid_end_date()

            project_controller.create_project()

            print_colored("\nProject created successfully\n", Colors.GREEN)

        elif choice == "2":
            project_controller.view_projects()

        elif choice == "3":
            project_controller.edit_project()

        elif choice == "4":
            project_controller.delete_project()

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