from modules.SqlHelpers import SqlHelpers
from modules.PostgreSqlHelpers import PostgreSqlHelpers
import os

class GetConnection():

    FILE_NAME= 'sqlconfig.txt'
    file_path = os.path.join("E:\Jimmii\Git\learning\python\database",FILE_NAME) 
    postgresqlconnectionstring =''
    sqlconnectiostring =''

    @staticmethod
    def LoadDataBaseConnection():
        SqlHelpers.LoadingFileConfig(GetConnection.file_path)
        PostgreSqlHelpers.LoadingFileConfig(GetConnection.file_path)    
        GetConnection.postgresqlconnectionstring = PostgreSqlHelpers.GetConnectionString()    
        GetConnection.sqlconnectiostring = SqlHelpers.GetConnectionString() 

def main():
    pass

if __name__ =='__main__':
    main()