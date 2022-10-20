from unittest import result
from flask import Blueprint, request, jsonify
from BL.departments_bl import departmentsBL

departments = Blueprint('departments', __name__)






@departments.route('/', methods=['GET'])
def get_all_departments():
    departments_bl = departmentsBL()
    departments = departments_bl.get_all_departments()
    return departments

@departments.route('/<id>', methods=['GET'])
def get_department(id):
    departments_bl = departmentsBL()
    department = departments_bl.get_department(id)
    return department

@departments.route('/<id>', methods=['PUT'])
def update_department(id):
    departments_bl = departmentsBL()
    obj = {
        "name":request.json["name"],
        "department_id":float(request.json["department_id"]),
        "employee_id":float(request.json["employee_id"]),
        
        }
    result = departments_bl.update_department(id, obj)
    return jsonify(result)

@departments.route('/', methods=['POST'])
def create_department():
    obj = {
        "department_id": float(request.json["department_id"]),
        "employee_id": float(request.json["employee_id"]),
        "name": request.json["name"],
        "employees": request.json["employees"]
    }
    departments_bl = departmentsBL()
    result = departments_bl.create_department(obj)
    return jsonify (result)
    
 
