from controllers.auth_controller import AuthController
from utils.get_valid_input import ValidInput
from utils.print_table import table_of_options

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

def main():
    
    auth_controller = AuthController()
    user_input = ValidInput()

    print_colored("\nWelcome to the Crowd-Funding App\n", Colors.MAGENTA)

    while True:
        choice = table_of_options("Please choose an option", "Login", "Register", "Exit")

        if choice == "1":
            
            email = user_input.get_valid_email(f"{Colors.RESET}Enter your email: {Colors.BLUE}")
            password = user_input.get_valid_passwords(f"{Colors.RESET}Enter your password: {Colors.BLUE}")

            user = auth_controller.login(email, password)
            if user:
                print_colored("\nYou have successfully logged in\n", Colors.GREEN)
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
            print_colored("\nGoodbye ^_^\n", Colors.CYAN)
            exit()
        
        else:
            print_colored("\nInvalid choice, please try again\n", Colors.RED)
    

if __name__ == "__main__":
    main()