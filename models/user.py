import json

class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone, id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone
        # self.projects = []
    
    def to_dect(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "mobile_phone": self.mobile_phone,
            # "projects": self.projects
        }
    
    @classmethod
    def find_by_email(cls, email):
        with open('data/users.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['email'] == email:
                    return cls(**user)
            return None
    @classmethod
    def find_by_id(cls, id):
        with open('data/users.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user['id'] == id:
                    return cls(**user)
            return None
    
    def check_password(self, password):
        return self.password == password
        
    # def save(self):
    #     with open('users.json', 'w+') as file:
    #         users = json.load(file)
    #         users.append(self.to_dect())
    #         json.dump(users, file)
