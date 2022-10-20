from flask import jsonify
from DAL.departments_dal import DepartmentsDAL
from DAL.employees_dal import EmployeesDAL


class departmentsBL:
    def __init__(self):
        self.__departments = DepartmentsDAL()
        self.__employees = EmployeesDAL()

    def get_all_departments(self):
        employees = self.__employees.get_all()
        departments = self.__departments.get_all_departments()
        for d in range(len(departments)):
            arr = []
            
            for e in range(len(employees)):
                if departments[d]["department_id"] == employees[e]["department_id"]:
                    obj = {"firstName": employees[e]["firstName"], "lastName":employees[e]["lastName"], "employee_id":employees[e]["employee_id"]}
                    arr.append(obj)
                    departments[d]["employees"] = arr
                    
                if departments[d]["employee_id"] == employees[e]["employee_id"]:
                    manager = {
                        "firstName": employees[e]["firstName"],
                        "lastName": employees[e]["lastName"],
                        "employee_id": employees[e]["employee_id"]}
                    departments[d]["manager"] = manager
            
                    
        return departments
                    
                    
            
                
                    
                    

    def get_department(self, id):
        department = self.__departments.get_department(int(id))
        return jsonify(department)

    def update_department(self, id, obj):
        result = self.__departments.update_department(id, obj)
        return result

    # create new department
    def create_department(self, obj):
        departments = self.__departments.get_all_departments()
        arr = list(filter(lambda x: x["department_id"]
                   == obj["department_id"], departments))
        if len(arr) > 0:
            return 'Department id already exist'
        else:
            result = self.__departments.create_department(obj)
            return result
