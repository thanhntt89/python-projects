from datetime import datetime
from flask import Blueprint, jsonify, request, make_response
import jwt

class AuthorityUtils():

    authority_bp = Blueprint('auth',__name__)

    def __init__(self):
        print('this is AuthorityUtils')

    @authority_bp.route('/')   
    def getToken():
        auth = request.authorization
        if auth and auth.password =='password':
            toke = jwt.endcode({'user':auth.username, 'exp': datetime.datetime.utcnow()+ datetime.timedelta(minutes=60)})
            return jsonify({'toke':toke.decode('utf-8')})
        return make_response('Could not verify!',401,{'WWW-Authenticate':'Basic realm ="Login required"'})


