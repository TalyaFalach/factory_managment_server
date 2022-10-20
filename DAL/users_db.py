from pymongo import MongoClient


class UsersDBDAL:
    def __init__(self) -> None:
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factory"]
        self.__collection = self.__db["users"]
        
    def get_all(self):
        users = list(self.__collection.find({}))
        return users
