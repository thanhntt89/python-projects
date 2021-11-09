from logutils import LogUtils
from flask import Flask
from modules.user import user
from modules.auth import auth
from modules.member import member
from modules.getconnection import GetConnection
class Server():

    API_VER = '/api/v2'
    app = Flask(__name__)    
    #app.config["DEBUG"] = True    
    #app.register_blueprint(auth.authority_bp, url_prefix='/api/v1/login/')   

    app.register_blueprint(auth.auth_bp, url_prefix = f'{API_VER}/auth/')
    app.register_blueprint(user.user_bp, url_prefix = f'{API_VER}/user/')   
    app.register_blueprint(member.member_bp, url_prefix = f'{API_VER}/member/')


def main():    

    #print('this main function')
    HOST ='localhost'
    PORT = 8888
    
    #Load connection string from file
    GetConnection.LoadDataBaseConnection()
    #Load logging configuration
    LogUtils.LoadLogConfiguration()

    server = Server()    
    server.app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()