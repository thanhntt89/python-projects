from flask import Flask
import pandas as pd


class Server():

    app = Flask(__name__)    
    app.config["DEBUG"] = True

    def __init__(self):
        print('this main server class')

    @app.route('/', methods=['GET'])
    def getUsers():
        return tuple([{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}])

def main():
    #print('this main function')
    HOST ='localhost'
    PORT = 8888
    server = Server()    
    server.app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()