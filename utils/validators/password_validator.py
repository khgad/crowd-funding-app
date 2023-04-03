from string import punctuation

class PasswordValidator:
    def __init__(self, max_length=8, uppercase=False, lowercase=False, digits=False, symbols=False):
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.digits = digits
        self.symbols = symbols
        self.length = max_length
    
    def is_valid(self, password, confirm_password=None):
        status = True
        message = "Invalid password. Please make sure it meets the following criteria:"
        if len(password) < self.length:
            message += f"\n- Must be at least {self.length} characters long"
            status = False
        if self.uppercase and not any(c.isupper() for c in password):
            message += f"\n- Must contain at least one uppercase letter"
            status = False
        if self.lowercase and not any(c.islower() for c in password):
            message += f"\n- Must contain at least one lowercase letter"
            status = False
        if self.digits and not any(c.isdigit() for c in password):
            message += f"\n- Must contain at least one digit"
            status = False
        if self.symbols and not any(p in password for p in punctuation):
            message += f"\n- Must contain at least one symbol letter"
            status = False
        
        if status:
            if confirm_password and password!= confirm_password:
                message = f"Passwords do not match"
                status = False
            else:
                message = "Valid Password"

        return (status, message)
        