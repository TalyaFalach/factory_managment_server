from requests import request
from DAL.employees_dal import EmployeesDAL
from DAL.departments_dal import DepartmentsDAL
from DAL.shifts_dal import ShiftsDAL
from flask import jsonify
from BL.auth_bl import AuthBL


class EmployeesBL:
    def __init__(self):
        self.__employees = EmployeesDAL()
        self.__departments = DepartmentsDAL()
        self.__shifts = ShiftsDAL()

#! get all
    def get_all_employees(self):
        employees = self.__employees.get_all()
        departments = self.__departments.get_all_departments()
        shifts = self.__shifts.get_all()

        arr = []
        for i in range(len(employees)):
            for x in range(len(departments)):
                if employees[i]["department_id"] == departments[x]["department_id"]:
                    employees[i]["department_name"] = departments[x]["name"]
                    arr.append(employees[i])

            for i in range(len(employees)):
                shifts_arr = []
                for x in range(len(shifts)):
                    for s in range(len(shifts[x]["employee"])):
                        if employees[i]["employee_id"] == shifts[x]["employee"][s]:
                            shifts_arr.append(
                                {"shift": shifts[x]["shift_id"], "date": shifts[x]["date"], "end_hour": shifts[x]["end_hour"], "start_hour":shifts[x]["start_hour"]})
                            employees[i]["shifts"] = shifts_arr
        return arr
    
#! get employee by id
    def get_employee(self, id):
        employees = self.get_all_employees()
        employee = list(
            filter(lambda x: x["employee_id"] == int(id), employees))
        return employee
#! update employee
    def update_employees(self, id, obj):
        employee = self.__employees.update_employee(int(id), obj)
        return employee

    def check_user(self, token):
        auth_bl = AuthBL()
        # exist = auth_bl.verify_token(token)
        # if exist == True:
        #     return True
        # else:
        #     return False
        exist = auth_bl.verify_token(token)
        return exist

#! create new employee
    def create_employee(self, obj):
        employees = self.__employees.get_all()
        arr = list(filter(lambda x: x["employee_id"]
                   == obj["employee_id"], employees))
        if len(arr) > 0:
            result = 'ID already exist'
        else:
            result = self.__employees.create_employee(obj)
        return result

    def delete_employee(self, id):
        result = self.__employees.delete_employee(id)
        shifts = self.__shifts.update_shifts(int(id))
        return jsonify(result)
    
    def add_employee_shift(self,emp_id, shift_id):
        self.__shifts.add_employee_shift(int(emp_id), int(shift_id))
        return 'Connected to new shift'
        
