from DAL.users_dal import UsersDAL
from flask import jsonify

class UsersBL:
    def __init__(self):
        self.__users = UsersDAL()
        
    def get_all_users(self):
        users = self.__users.get_all_users()
        return jsonify(users)
    
    
