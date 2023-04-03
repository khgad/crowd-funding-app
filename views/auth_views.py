from utils.colors import *
from utils.get_valid_input import ValidInput

def login(auth_controller, user_input):
    email = user_input.get_valid_email(f"{Colors.RESET}Enter your email: {Colors.BLUE}")
    password = user_input.get_valid_passwords(f"{Colors.RESET}Enter your password: {Colors.BLUE}")

    user = auth_controller.login(email, password)
    if user:
        print_colored("\nYou have successfully logged in\n", Colors.GREEN)
    else:
        print_colored("\nInvalid email or password\n", Colors.RED)
    return user

def register(auth_controller, user_input):
    first_name = user_input.get_valid_name(f"{Colors.RESET}Enter your first name: {Colors.BLUE}")
    last_name = user_input.get_valid_name(f"{Colors.RESET}Enter your last name: {Colors.BLUE}")
    email = user_input.get_valid_email(f"{Colors.RESET}Enter your email: {Colors.BLUE}")
    password = user_input.get_valid_passwords(f"{Colors.RESET}Enter your password: {Colors.BLUE}")
    # confirm_password = user_input.get_valid_passwords("Confirm your password: {Colors.BLUE}")
    mobile_phone = user_input.get_valid_phone(f"{Colors.RESET}Enter your mobile phone number: {Colors.BLUE}")

    auth_controller.register(first_name, last_name, email, password, mobile_phone)

    print_colored("\nYou have successfully registered\n", Colors.GREEN)

def exit_app():
    print_colored("\nThank you for using Crowd-Funding App\n", Colors.GREEN)
    print_colored("Goodbye ^_^\n", Colors.CYAN)
    exit()

def logout():
    pass