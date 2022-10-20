import json
from flask import Blueprint, jsonify, request, make_response
from BL.shifts_bl import shiftsBL
shifts = Blueprint('shifts', __name__)

shifts_bl = shiftsBL()


@shifts.route('/', methods=['GET'])
def get_all():
    data = shifts_bl.get_all_shifts()
    return data


@shifts.route('/<id>', methods=['GET'])
def get_shift(id):
    data = shifts_bl.get_shift(int(id))
    return data


@shifts.route('/<id>', methods=['PUT'])
def update_shift(id):
    data = shifts_bl.update_shift(id)
    return data


@shifts.route('/', methods=['POST'])
def create_shift():
    employee = []
    for i in request.json["employee"]:
        employee.append(float(i))

    obj = {
        "shift_id": float(request.json["shift_id"]),
        "date": request.json["date"],
        "start_hour": float(request.json["start_hour"]),
        "end_hour": float(request.json["end_hour"]),
        "employee": employee
    }
    result = shifts_bl.create_shift(obj)
    return jsonify(result)


@shifts.route('/<emp_id>/<shift_id>', methods=['DELETE'])
def delete_employee_from_shift(emp_id, shift_id):
    result = shifts_bl.remove_employee(emp_id, shift_id)
    return jsonify(result)
