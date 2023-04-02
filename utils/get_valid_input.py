from utils.validators.email_validator import EmailValidator
from utils.validators.phone_validator import PhoneValidator
from utils.validators.password_validator import PasswordValidator

class ValidInput:
    
    def get_valid_name(self, prompt_message):
        while True:
            name = input(prompt_message)
            if len(name) > 0 and name.isalpha():
                return name
            else:
                print(f"\n\033[0;31mPlease enter a valid name.\033[0;0m\n")

    def get_valid_email(self, prompt_message):
        email_validator = EmailValidator()
        while True:
            email = input(prompt_message)
            status, message = email_validator.is_valid(email)
            if status:
                return email
            else:
                print(f"\n\033[0;31m{message}\033[0;0m\n")

    def get_valid_phone(self, prompt_message):
        phone_validator = PhoneValidator()
        while True:
            phone = input(prompt_message)
            status, message = phone_validator.is_valid(phone)
            if status:
                return phone
            else:
                print(f"\n\033[0;31m{message}\033[0;0m\n")
    
    def get_valid_passwords(self, prompt_message):
        password_validator = PasswordValidator()
        while True:
            password = input(prompt_message)
            status, message = password_validator.is_valid(password)
            if status:
                return password
            else:
                print(f"\n\033[0;31m{message}\033[0;0m\n")
    