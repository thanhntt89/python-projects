import pyodbc as odbc
import pandas as pd
class SqlHelpers(object):
    #Default connection information
    SERVER = 'WINSERVER2016'
    USER_NAME = 'wiiAdmin'
    PASSWORDS = 'W_iiAdmin00000'
    DATABASE = 'Wii'
    COMMAND_TIMEOUT = 5000

    connection_string = 'DRIVER={SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER_NAME+';PWD='+ PASSWORDS
    
    @staticmethod
    def GetConnectionString():
        SqlHelpers.connection_string = 'DRIVER={SQL Server};SERVER='+SqlHelpers.SERVER+';DATABASE='+SqlHelpers.DATABASE+';UID='+SqlHelpers.USER_NAME+';PWD='+ SqlHelpers.PASSWORDS 
        return SqlHelpers.connection_string

    @staticmethod
    def test_connection(connection_string):        
        try:            
            con = odbc.connect(connection_string)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT
            cur = con.cursor()
            cur.open()  
            cur.closest()
            return True
        except:
            return False
    
    #Get data in table from database
    #Return columns, data row
    @staticmethod
    def ExecuteDataset(connection_string,query):
        con = odbc.connect(connection_string)
        con.timeout = SqlHelpers.COMMAND_TIMEOUT
        cur = con.cursor()        
        cur.execute(query) 
        dat_row = cur.fetchall()
        columns = [cols[0] for cols in cur.description]
        return [columns,dat_row]

    @staticmethod
    def ExecutePandas(connection_string, query):
        con = odbc.connect(connection_string)
        con.timeout = SqlHelpers.COMMAND_TIMEOUT
        cur = con.cursor()
        data = pd.read_sql_query(query,con)
        return data

    @staticmethod
    def ExecuteNonQuery(connection_string, query):
        try:
            con = odbc.connect(connection_string)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT
            cur = con.cursor() 
            cur.execute(query)
        except ValueError as e:
            raise e.__traceback__
             

def main():
    SqlHelpers.SERVER ='WINSERVER2016'
    SqlHelpers.DATABASE ='Wii'
    SqlHelpers.PASSWORDS ='W_iiAdmin00000' 
    SqlHelpers.USER_NAME ='wiiAdmin'    
    connection_string = SqlHelpers.GetConnectionString()
    #print('Test connected:' + str(SqlHelpers.test_connection(connection_string)))

    #test execute datasets
    #test_executedataset(connection_string)
    Test_ExecutePandas(connection_string)
    #test_executenonquery(connection_string)


def Test_ExecutePandas(connection_string):
    try: 
        query ='EXEC [dbo].[select_test]'
        data = SqlHelpers.ExecutePandas(connection_string,query)
        print(data)
        print(type(data))
    except ValueError as e:
        print(f'error exception:{e}')

def test_executenonquery(connection_string):
    try:    
        print('Sql connection string :'+ connection_string)
        print('Test connected:' + str(SqlHelpers.test_connection(connection_string)))
        query ='INSERT INTO [FestaVideoLock]([ContentType]) VALUES(12)'
        SqlHelpers.ExecuteNonQuery(connection_string,query)
    except ValueError as e:
        print(f'error exception:{e}')

def test_executedataset(connection_string):    
    print('Sql connection string :'+ connection_string)
    query = 'EXEC [dbo].[select_test]'
    columns , user_group_dataset = SqlHelpers.ExecuteDataset(connection_string, query)

    print('User_groups:\n')
    print(columns)
    #print(user_group)
    for ug in user_group_dataset:
        print(ug)

if __name__ == "__main__":
    main()
