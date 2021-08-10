from flask import Flask, jsonify
import pandas as pd
from modules.user import user

class Server():

    app = Flask(__name__)    
    app.config["DEBUG"] = True
    user = user()
    app.register_blueprint(user.user_bp, url_prefix='/user')

    def __init__(self):
        print('this main server class')

    @app.route('/', methods=['GET'])
    def getUsers():
        return jsonify([{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]), 200

    @app.route('/<string:name>')
    def hello(name):
        return f'Hello {name}'
    


def main():
    #print('this main function')
    HOST ='localhost'
    PORT = 8888
    server = Server()    
    server.app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()