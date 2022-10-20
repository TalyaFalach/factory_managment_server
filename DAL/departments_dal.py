from pymongo import MongoClient

class DepartmentsDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factory"]
        self.__collection = self.__db["departments"]
        
        # get all
    def get_all_departments(self):
        data = list(self.__collection.find({}))
        return data
    
        # get by id
    def get_department(self,id):
        data = list(self.__collection.find({"department_id": int(id)}))
        return data
    
    
    
        # update department
    def update_department(self, id, obj):
        self.__collection.update_one({"department_id": int(id)}, {"$set": obj})
        return 'updated'
    
        #create new department
    def create_department(self, obj):
        self.__collection.insert_one(obj)
        return 'Created !'
        
    