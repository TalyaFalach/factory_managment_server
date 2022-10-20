from os import remove
from pymongo import MongoClient


class ShiftsDAL:
    def __init__(self) -> None:
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["factory"]
        self.__collection = self.__db["shifts"]

    def get_all(self):
        shifts = list(self.__collection.find({}))
        return shifts

    def get_shift(self, id):
        shift = self.__collection.find_one({"shift_id": int(id)})
        return shift

    def create_shift(self, obj):
        self.__collection.insert_one(obj)
        return 'Created !'

    def update_shifts(self, id):
        indexes = []
        shifts = list(self.__collection.find({"employee": id}))
        for i in shifts:
            i["employee"].remove(id)
            indexes.append(i["shift_id"])

        for i in range(len(indexes)):
            self.__collection.find_one_and_delete({"shift_id": indexes[i]})
            self.__collection.insert_one(shifts[i])

        return 'Updated Shifts'

    def add_employee_shift(self, emp_id, shift_id):
        shift = self.__collection.find_one({"shift_id": shift_id})
        shift["employee"].append(float(emp_id))
        shift_to_delete = self.__collection.delete_one({"shift_id": shift_id})
        updated_shift = self.__collection.insert_one(shift)
        return updated_shift
    
    def remove_employee(self,emp_id, shift_id):
        shift = self.__collection.update_one({"shift_id": shift_id},{"$pull":{"employee":emp_id}})
        return 'Deleted'
        


    
