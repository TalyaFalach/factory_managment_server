from flask import Blueprint,jsonify, request, make_response
from BL.auth_bl import AuthBL

auth = Blueprint('auth', __name__)

auth_bl = AuthBL()

@auth.route('/login', methods=['POST'])
def login():
    username = request.json["username"]
    email = request.json["email"]
    
    token = auth_bl.get_token(username,email)
    if token is not None:
        return make_response({"token":token}, 200)
    else:
        return make_response({"error":"error"}, 401)
    


