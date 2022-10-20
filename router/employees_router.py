import json
from numbers import Number
from unittest import result
from flask import Blueprint, jsonify, request, make_response
from BL.employees_bl import EmployeesBL
employees = Blueprint('employees', __name__)

employees_bl = EmployeesBL()


@employees.route('/', methods=['GET'])
def get_all_employees():

    if request.headers and request.headers.get('x-access-token'):
        token = request.headers.get('x-access-token')
        exist = employees_bl.check_user(token)

        if exist != None:
            employees = employees_bl.get_all_employees()
            return make_response({"employees": employees}, 200)
        else:
            return make_response({"error": "no token provided"}, 401)
    else:
        return make_response({"error": "no token provided"}, 401)


# @employees.route('/<id>', methods=['GET'])
# def get_employee(id):
#     employee = employees_bl.get_employee(int(id))
#     return employee



@employees.route('/<id>', methods=['GET'])
def get_employee(id):
    if request.headers and request.headers.get('x-access-token'):
        token = request.headers.get('x-access-token')
        exist = employees_bl.check_user(token)

        if exist != None:
            employee = employees_bl.get_employee(int(id))
            return make_response({"employees": employee}, 200)
        else:
            return make_response({"error": "no token provided"}, 401)
    else:
        return make_response({"error": "no token provided"}, 401)




@employees.route('/<id>', methods=['PUT'])
def update_employee(id):
    obj = {"firstName": request.json["firstName"], "lastName": request.json["lastName"], "employee_id": float(
        request.json["employee_id"]), "start_work_year": float(request.json["start_work_year"]), "department_id": float(request.json["department_id"])}
    result = employees_bl.update_employees(id, obj)
    return jsonify(result)


@employees.route('/', methods=['POST'])
def create_employee():
    obj = {
        "employee_id":float(request.json["employee_id"]),
        "firstName":request.json["firstName"],
        "lastName":request.json["lastName"],
        "start_work_year":float(request.json["start_work_year"]),
        "department_id":float(request.json["department_id"]),
        "shifts": request.json["shifts"]
        }
    result = employees_bl.create_employee(obj)
    return jsonify(result)

@employees.route('/<id>',methods=['DELETE'])
def delete_employee(id):
    result = employees_bl.delete_employee(int(id))
    return result

@employees.route('/shift/<emp_id>/<shift_id>',methods=['PUT'])
def add_employee_shift(emp_id, shift_id):
    result = employees_bl.add_employee_shift(emp_id, shift_id)
    return jsonify(result)




