import re

class PhoneValidator:
    def __init__(self, pattern = None):
        if pattern is None:
            self.phone_pattern = re.compile(r"^01[0125][0-9]{8}$")
        else:
            self.phone_pattern = re.compile(pattern)
    
    def is_valid(self, phone):
        if re.match(self.phone_pattern, phone):
            return (True, "Valid phone number")
        else:
            return (False, "Invalid phone number. Please enter a valid Egyptian phone number.")