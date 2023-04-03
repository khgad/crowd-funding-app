import re
from controllers.auth_controller import AuthController

class EmailValidator:
    def __init__(self, pattern = None):
        if pattern is None:
            self.email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        else:
            self.email_pattern = re.compile(pattern)
    
    def is_valid(self, email, registration = False):
        if not re.match(self.email_pattern, email):
            return (False, "Invalid email address. Please enter a valid email address. ex: example@example.com")
        elif registration and not AuthController().is_email_unique(email):
            return (False, "This email address is already in use")
        return (True, "Valid email address")