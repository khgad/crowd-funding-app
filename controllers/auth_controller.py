from models.user import User
from utils.file_operations import *
import json

class AuthController:

    users_filename = 'data/users.json'
    
    def register(self, first_name, last_name, email, password, mobile_phone):
        new_user = User(first_name, last_name, email, password, mobile_phone)
        status = new_user.save()
        # self.save_user_to_file(new_user)
        return new_user
    
    def login(self, email, password):
        user = User.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None
    
    def is_email_unique(self, email):
        user = User.find_by_email(email)
        if user:
            return False
        return True

    # def save_user_to_file(self, new_user):
    #     users = read_json_file(self.users_filename)
    #     new_user.id = get_next_id(users)
    #     users.append(new_user.to_dect())
    #     write_json_file(self.users_filename, users)
        # with open('data/users.json', 'r+') as file:
        #     users = json.load(file)
        #     new_user = new_user
        #     if len(users) == 0:
        #         new_id = 0
        #     else:
        #         new_id = users[-1]['id'] +1
        #     new_user.id = new_id
        #     users.append(new_user.to_dect())
        #     file.seek(0)    # Move the file pointer to the beginning of the file
        #     json.dump(users, file)