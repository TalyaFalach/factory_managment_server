from DAL.users_db import UsersDBDAL
from flask import jsonify


class UsersDBBL:
    def __init__(self):
        self.__users = UsersDBDAL()

    def get_all_shifts(self):
        users = self.__users.get_all()
        return jsonify(users)

