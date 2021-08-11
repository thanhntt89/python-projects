from flask import Blueprint, jsonify, request
from modules.SqlHelpers import SqlHelpers

class user():

    #User router 
    user_bp = Blueprint('user',__name__)
    
    def __init__(self):
        self.user_bp = Blueprint('user',__name__)
        print('this user class')
    
    @user_bp.route('/')
    def index():
        return jsonify('this is user index')

    @user_bp.route('/list/')
    def users():
        key = request.headers.get('key')
        print(f'key: {key}')
        key_body = request.form.get('key_body')
        print(f'key_body: {key_body}')
        query = f'SELECT [利用者ID] as user_id ,[権限グループ] as user_name ,[利用者名] as role  FROM [Wii].[dbo].[Fes利用者]'        
        df = SqlHelpers.ExecuteDataFrame(SqlHelpers.GetConnectionString(), query)
        return df.to_json(orient="records")

def main():
    print('this main user class')

if __name__ == '__main__':
    main()