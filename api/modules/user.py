from flask import Blueprint, jsonify

class user():

    #User router 
    user_bp = Blueprint('user',__name__)
    
    def __init__(self):
        self.user_bp = Blueprint('user',__name__)
        print('this user class')
    
    @user_bp.route('/')
    def index():
        return jsonify('this is user index')


def main():
    print('this main user class')

if __name__ == '__main__':
    main()