###########################################################################
#Install: flask, pyjwt, datetime, Flask-JWT-Extended==4.1.0 to use decoded tokens
#Check token validity for method to protected endpoint
#Use: set before function 
#@auth.token_required
#def functionName():
###########################################################################
from configparser import Error
import datetime
from flask import Blueprint, jsonify, request, make_response
import jwt
from functools import wraps
class auth():
    #Define the route
    auth_bp = Blueprint('auth',__name__)

    SECRET_KEY = 'jimmii88'

    USER_DEFAULT = 'admin'
    PASSWORD_DEFAULT = 'password'

    def __init__(self) -> None:
        pass
    
    ################################
    # Define the method check for methods that to require token access
    ################################
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.args.get('token', None)
            #print('token_request: '+token)
            if not token:
                return jsonify({'message':'Token is missing'}), 403 

            try:
                data = jwt.decode(token,auth.SECRET_KEY,algorithms=["HS256"])#, options={"verify_exp": False}
            except ValueError as e:
               #print('error:'+e.message)
               return jsonify({'message':'Token is missing or invalid'}), 403

            return f(*args, **kwargs)

        return decorated


    ################################
    #Get token by login user
    ################################
    @auth_bp.route('/token', methods=['POST', 'GET'])
    def getToken():
        authority = request.authorization
        #print (f'user: {authority.username} password: {authority.password}')

        if authority and authority.username == auth.USER_DEFAULT and authority.password == auth.PASSWORD_DEFAULT:
            token = jwt.encode({'user':authority.username, 'exp': datetime.datetime.now() + datetime.timedelta(minutes=60)}, auth.SECRET_KEY)   
            return jsonify({'token': token.encode().decode('UTF-8')})

        return make_response('Could not verify!',401,{'WWW-Authenticate':'Basic realm ="Login required"'})
