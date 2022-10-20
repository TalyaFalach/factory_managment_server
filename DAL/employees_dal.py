from pymongo import MongoClient

class EmployeesDAL:
    def __init__(self) -> None:
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factory"]
        self.__collection = self.__db["employees"]
        
    # def get_all(self,fname):
    #     if fname !=None:
    #         employee = list(self.__collection.find({"firstName":fname}))
    #         return employee
    #     else:
    #         employees = list(self.__collection.find({}))
    #         return employees
    def get_all(self):
        employees = list(self.__collection.find({}))
        return employees
        
    
    def get_employee(self, id):
        employee = self.__collection.find_one({"employee_id": int(id)})
        return employee
    
    def update_employee(self, id, obj):
        self.__collection.update_one({"employee_id": int(id)}, {"$set": obj})
        return 'Updated'
    
    
    #!Create new employee    
    def create_employee(self,obj):
        self.__collection.insert_one(obj)
        return 'Created !'
    
    def delete_employee(self,id):
        
        self.__collection.delete_one({"employee_id":int(id)})
        return 'Deleted !'