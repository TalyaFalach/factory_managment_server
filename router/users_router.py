from flask import Blueprint
from BL.users_bl import UsersBL
users_bl = UsersBL()

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_all_users():
    users_bl = UsersBL()
    users = users_bl.get_all_users()
    return users