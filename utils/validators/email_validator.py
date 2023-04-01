import re

class EmailValidator:
    def __init__(self, pattern = None):
        if pattern is None:
            self.email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        else:
            self.email_pattern = re.compile(pattern)
    
    def is_valid(self, email):
        if re.match(self.email_pattern, email):
            return (True, "Valid email address")
        else:
            return (False, "Invalid email address. Please enter a valid email address. ex: example@example.com")