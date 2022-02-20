from flask import Blueprint , jsonify, request, make_response
import flask
from modules.PostgreSqlHelpers import PostgreSqlHelpers
from modules.getconnection import GetConnection
from modules.auth import auth
from logutils import LogUtils
class member():

    member_bp = Blueprint('member',__name__)

    def __init__(self):
        pass

    @member_bp.route('/',methods =['GET','POST'])
    def getMember():
        query = 'select * from member'       
        df = PostgreSqlHelpers.ExecuteDataFrame(GetConnection.postgresqlconnectionstring,query)
        return df.to_json(orient="records")
        return 'ok'

    @member_bp.route('/add',methods =['POST'])
    @auth.token_required
    def addMember():
        try:
            data = flask.request.json
            username = data['username']
            fullname =  data['fullname']
            email = data['email']
            query = 'insert into member (username, fullname, email) values(%s, %s, %s)'
            parameters = (username,fullname,email)        
            PostgreSqlHelpers.ExecuteNonQueryWithParameters(GetConnection.postgresqlconnectionstring,query,parameters)
            return make_response('Add successfully',200)
        except ValueError as e:
            return make_response(jsonify({"error_code":400,"message":e.args}), 200)

    @member_bp.route('/delete',methods =['POST'])
    @auth.token_required
    def deleteMember():        
        try:

            data = flask.request.json
            username = data['username']
            query = 'delete from member where username = %s'
            parameters = ("'%s'"%username)
            query = query%parameters
            #print("query:" + query)
            LogUtils.logInfo(f'Request delete member id={username} ')

            #Step1: Check username exist in table
            query_select = 'select username from member where username = %s'%(f"'{username}'")
            df = PostgreSqlHelpers.ExecuteDataFrame(GetConnection.postgresqlconnectionstring,query_select)
            
            if df.empty:
                return make_response(f'username: {username} not found',200)

            PostgreSqlHelpers.ExecuteNonQueryWithParameters(GetConnection.postgresqlconnectionstring,query,parameters)
            return make_response('Delete successfully',200)
        except ValueError as e:
            return make_response(jsonify({"error_code":400,"message":f"System error {e.message}"}),403)