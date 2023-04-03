from utils.validators.email_validator import EmailValidator
from utils.validators.phone_validator import PhoneValidator
from utils.validators.password_validator import PasswordValidator
from utils.validators.date_validator import DateValidator
import datetime

class ValidInput:
    
    def get_valid_name(self, prompt_message):
        while True:
            name = input(prompt_message)
            if len(name) > 0 and name.isalpha():
                return name
            else:
                print(f"\n\033[0;31mPlease enter a valid name.\033[0;0m\n")

    def get_valid_email(self, prompt_message, registration = False):
        email_validator = EmailValidator()
        while True:
            email = input(prompt_message)
            status, message = email_validator.is_valid(email, registration)
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
    
    def get_valid_passwords(self, prompt_message, confirm_password = None):
        password_validator = PasswordValidator()
        while True:
            password = input(prompt_message)
            status, message = password_validator.is_valid(password, confirm_password)
            if status:
                return password
            else:
                print(f"\n\033[0;31m{message}\033[0;0m\n")
    
    def get_valid_title(self, prompt_message):
        while True:
            title = input(prompt_message)
            if len(title) > 0:
                return title
            else:
                print(f"\n\033[0;31mPlease enter a valid title.\033[0;0m\n")

    def get_valid_description(self, prompt_message):
        while True:
            description = input(prompt_message)
            if len(description) > 0:
                return description
            else:
                print(f"\n\033[0;31mPlease enter a valid description.\033[0;0m\n")
    
    def get_valid_target_money(self, prompt_message):
        while True:
            target_money = input(prompt_message)
            if len(target_money) > 0 and target_money.isdigit():
                return target_money
            else:
                print(f"\n\033[0;31mPlease enter a valid target money.\033[0;0m\n")
    
    def get_valid_date(self, prompt_message, not_before = None, not_after = None):
        date_validator = DateValidator()
        while True:
            date_str = input(prompt_message)
            status, message = date_validator.is_valid(date_str, not_before, not_after)
            if status:
                return date_str
            else:
                print(f"\n\033[0;31m{message}\033[0;0m\n")
