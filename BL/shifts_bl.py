from DAL.shifts_dal import ShiftsDAL
from DAL.employees_dal import EmployeesDAL
from flask import jsonify


class shiftsBL:
    def __init__(self):
        self.__shifts = ShiftsDAL()
        self.__employees = EmployeesDAL()


    def get_all_shifts(self):
        shifts = self.__shifts.get_all()
        return jsonify(shifts)
    
    def get_shift(self, id):
        shift = self.__shifts.get_shift(id)
        return shift
    
    def create_shift(self,obj):
        shift = self.__shifts.create_shift(obj)
        return shift
    
    def remove_employee(self, emp_id,shift_id):
        result = self.__shifts.remove_employee(int(emp_id), int(shift_id))
        return result

        
