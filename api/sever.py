from flask import Flask
import pandas as pd
from modules.user import user

class Server():

    app = Flask(__name__)    
    #app.config["DEBUG"] = True    
    app.register_blueprint(user.user_bp, url_prefix='/user/')
  


def main():
    #print('this main function')
    HOST ='localhost'
    PORT = 8888
    server = Server()    
    server.app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()