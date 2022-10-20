import requests
class UsersDAL:
    def __init__(self):
        self.__url = 'https://jsonplaceholder.typicode.com/users'
        
    def get_all_users(self):
        res = requests.get(self.__url)
        data = res.json()
        return data