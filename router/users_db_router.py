import json
from flask import Blueprint, jsonify, request, make_response
from BL.users_db_bl import UsersDBBL
usersdb = Blueprint('usersdb', __name__)

users_db_bl = UsersDBBL()


@usersdb.route('/', methods=['GET'])
def get_all():
    data = users_db_bl.get_all_shifts()
    return data
