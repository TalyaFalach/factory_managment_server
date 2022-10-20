import jwt
from DAL.users_dal import UsersDAL


class AuthBL:
    def __init__(self):
        self.__key = "server_key"
        self.__algorithm = "HS256"

    def get_token(self, username, email):
        user_id = self.__check_user(username, email)
        token = None
        if user_id is not None:
            token = jwt.encode({"user_id": user_id},
                               self.__key, self.__algorithm)
        return {"token": token, "user_id": user_id}


    def __check_user(self, username, email):
        users_dal = UsersDAL()
        users = users_dal.get_all_users()
        for user in users:
            if user["username"] == username and user["email"] == email:
                user_id = user["id"]
                return user_id

    def verify_token(self, token):
        data = jwt.decode(token, self.__key, self.__algorithm)
        user_id = data["user_id"]
        users_dal = UsersDAL()
        users = users_dal.get_all_users()

        for user in users:
            if user["id"] == user_id:
                return True
            else:
                return False
