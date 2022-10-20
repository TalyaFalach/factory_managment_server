import json
from flask import Flask
from bson import ObjectId
from flask_cors import CORS
from router.auth_router import auth
from router.employees_router import employees
from router.users_router import users
from router.departments_router import departments
from router.shifts_router import shifts
from router.users_db_router import usersdb

app = Flask(__name__)


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app.json_encoder = JSONEncoder

 
app.url_map.strict_slashes = False

CORS(app)
app.register_blueprint(users, url_prefix='/users')

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(employees, url_prefix='/employees')
app.register_blueprint(departments, url_prefix='/departments')
app.register_blueprint(shifts, url_prefix='/shifts')
app.register_blueprint(usersdb, url_prefix='/usersdb')
app.run()


# {
    # "employee_id": 10.0,
    # "firstName": "Clementina",
    # "lastName": "DuBuque",
    # "start_work_year": 2010.0,
    # "department_id": 2.0,
#     "_id": ObjectId("634e5c4b14d7386cb7dd02b0")
# }
