############################################################
#SqlHelpers is class suport for connectting with SQL Server
#Supported with transaction, return pandas object, dict object 
#Support reading connection info from files config 
#File config example: 
#[DATABASE]
#SERVER = SERVER
#USER_NAME = USER_NAME
#PASSWORD = PASSWORD
#CONNECTION_TIMEOUT =CONNECTION_TIMEOUT
#COMMAND_TIMEOUT = COMMAND_TIMEOUT
############################################################
#Created by: Nguyen Tat Thanh (Jimmii88)
#Email: thanhntt89bk@gmail.com
#Link: https://github.com/thanhntt89/python-projects/blob/main/database/SqlHelpers.py
#Created date: 2021/08/08
############################################################
import os
import pyodbc as odbc
import pandas as pd
from configparser import ConfigParser

class SqlHelpers(object):
    #Default connection information
    SERVER = ''
    USER_NAME = ''
    PASSWORDS = ''
    DATABASE = ''
    PORT = 1433
    #Time out execute query 
    COMMAND_TIMEOUT = 5000
    #Time out check connection
    CONNECTION_TIMEOUT = 300

    #Default connection string
    connection_string = 'DRIVER={SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER_NAME+';PWD='+ PASSWORDS
    
    #transaction variable
    transaction = ''

    #Create transaction object
    @staticmethod
    def CreateTransaction(connection_string):
        try:
            con = odbc.connect(connection_string, autocommit=False)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT     
            SqlHelpers.transaction = con.cursor()           
        except ValueError as e:
            raise e.args

    ################################################################
    #Add query to transaction
    ################################################################
    @staticmethod
    def TransactionAdd(query):
        SqlHelpers.transaction.execute(query)

    ################################
    #Add query to transaction with parameters
    ################################
    @staticmethod
    def TransactionAddWithParameters(query, parameters):
        SqlHelpers.transaction.execute(query, parameters)

    ################################################################
    #Transaction committing to database
    ################################################################
    @staticmethod
    def TransactionCommitting():
        try:
            SqlHelpers.transaction.commit()       
        except ValueError as e:
            SqlHelpers.transaction.rollback() 
            raise e.args
    
    #########################
    #Create connection string
    #########################
    @staticmethod
    def GetConnectionString():
        SqlHelpers.connection_string = 'DRIVER={SQL Server};SERVER='+SqlHelpers.SERVER+','+str(SqlHelpers.PORT)+';DATABASE='+SqlHelpers.DATABASE+';UID='+SqlHelpers.USER_NAME+';PWD='+ SqlHelpers.PASSWORDS+';Time out = '+ str(SqlHelpers.CONNECTION_TIMEOUT)
        return SqlHelpers.connection_string

    @staticmethod
    def test_connection(connection_string):        
        try:            
            con = odbc.connect(connection_string)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT            
            cur = con.cursor()
            cur.execute("select @@VERSION")
            return True
        except:
            return False
    
    ################################################################
    #Get data in table from database
    #Return dict data
    ################################################################
    @staticmethod
    def ExecuteDict(connection_string,query):
        try:
            con = odbc.connect(connection_string)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT
            cur = con.cursor()        
            cur.execute(query) 
            dat_row = cur.fetchall()
            columns = [cols[0] for cols in cur.description] 
            data = [dict(zip(columns, row)) for row in dat_row]
            return data 
        except Exception as e:
            raise e.args

    @staticmethod
    def ExecuteDataFrame(connection_string, query):
        try:    
            con = odbc.connect(connection_string)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT
            cur = con.cursor()
            data = pd.read_sql_query(query,con)
            return data
        except Exception as e:            
            raise e.args

    ###############################
    # SQL running with query parameter character ? and values array
    ###############################
    @staticmethod
    def ExecuteNonQueryWithParameters(connection_string, query,vales):
        try:
            con = odbc.connect(connection_string)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT           
            cur = con.cursor() 
            cur.execute(query, vales)   
            con.close()
        except ValueError as e:
            con.rollback()
            con.close()
            raise e.__traceback__

    #########################
    # SQL running query without parameters
    #########################
    @staticmethod
    def ExecuteNonQuery(connection_string, query):
        try:
            con = odbc.connect(connection_string, autocommit = True)
            con.timeout = SqlHelpers.COMMAND_TIMEOUT           
            cur = con.cursor() 
            cur.execute(query)            
            cur.close()
            con.close()
        except ValueError as e:
            cur.close()
            con.rollback()
            con.close()
            raise e.__traceback__

    #########################
    #Load file config file
    #Info config file:
    #Line 1: [SQLCONFIG]
    #Line 2: SERVER = SERVER NAME
    #Line 4: USER_NAME = USER_NAME
    #Line 5: PASSWORDS = PASSWORD
    #Line 6: DATABASE = DATABASE
    #Line 7: TIMEOUT = TIMEOUT
    #########################
    @staticmethod
    def LoadingFileConfig(config_file_path):
        try:
            config = ConfigParser()
            config.read(config_file_path)          

            SqlHelpers.SERVER = config.get('SQLCONFIG','SERVER')
            SqlHelpers.USER_NAME = config.get('SQLCONFIG','USER_NAME')
            SqlHelpers.PASSWORDS = config.get('SQLCONFIG','PASSWORD')
            SqlHelpers.DATABASE = config.get('SQLCONFIG','DATABASE')
            SqlHelpers.COMMAND_TIMEOUT = int(config.get('SQLCONFIG','COMMAND_TIMEOUT')) 
            SqlHelpers.CONNECTION_TIMEOUT = int(config.get('SQLCONFIG','CONNECTION_TIMEOUT'))
            SqlHelpers.PORT = int(config.get('SQLCONFIG','PORT'))
        except ValueError as e:
            raise e.args


def main():
    SqlHelpers.SERVER ='WINSERVER2016'
    SqlHelpers.DATABASE ='Wii'
    SqlHelpers.PASSWORDS ='W_iiAdmin00000' 
    SqlHelpers.USER_NAME ='wiiAdmin'    
    Test_LoadingFileConfig()
    connection_string = SqlHelpers.GetConnectionString()
    print('connection string: '+ connection_string)
    print('Test connected:' + str(SqlHelpers.test_connection(connection_string)))
    #Test loading config 
   
    #test execute datasets
    Test_ExecuteDict(connection_string)
    #Test_ExecuteDataFrame(connection_string)
    #Test_ExecuteNonQuery(connection_string)
    #Test_Transaction(connection_string)

def Test_LoadingFileConfig():
    FILE_NAME= 'sqlconfig.txt'
    file_path = os.path.join(os.path.dirname(__file__),FILE_NAME) 
    SqlHelpers.LoadingFileConfig(file_path)
    connection_string = SqlHelpers.GetConnectionString()
    print('Connection string: %s' % connection_string) 

def Test_Transaction(connection_string):
    SqlHelpers.CreateTransaction(connection_string)
    query ='INSERT INTO dbo.[FestaVideoLock]([ContentType]) VALUES(14)'     
    query1 ='INSERT INTO dbo.[FestaVideoLock]([ContentType]) VALUES(15)'  
    SqlHelpers.TransactionAdd(query)
    SqlHelpers.TransactionAdd(query1) 

    query2 ='INSERT INTO dbo.[FestaVideoLock]([ContentType]) VALUES(?)' 
    value2 = 16
    query3 ='INSERT INTO dbo.[FestaVideoLock]([ContentType]) VALUES(?)'
    value3 = 17
    SqlHelpers.TransactionAddWithParameters(query2,value2)
    SqlHelpers.TransactionAddWithParameters(query3,value3)

    SqlHelpers.TransactionCommitting()

def Test_ExecuteDataFrame(connection_string):
    try: 
        query ='EXEC [dbo].[select_test]'
        data = SqlHelpers.ExecuteDataFrame(connection_string,query)
        print(data)
        print(type(data))
    except ValueError as e:
        print(f'error exception:{e}')

def Test_ExecuteNonQuery(connection_string):
    try:           
        query ='INSERT INTO dbo.[FestaVideoLock]([ContentType]) VALUES(?)'     
        values =('14')

        SqlHelpers.ExecuteNonQueryWithParameters(connection_string,query,values)  
        query ='INSERT INTO dbo.[FestaVideoLock]([ContentType]) VALUES(15)'   
        SqlHelpers.ExecuteNonQuery(connection_string,query) 
    except ValueError as e:
        print(f'error exception:{e}')

def Test_ExecuteDict(connection_string):    
    print('Sql connection string :'+ connection_string)
    query = 'EXEC [dbo].[select_test]'
    user_group_dataset = SqlHelpers.ExecuteDict(connection_string, query)

    print('User_groups:\n')
    #print(columns)
    print(user_group_dataset)
    # for ug in user_group_dataset:
    #     print(ug)

    print(type(user_group_dataset))

if __name__ == "__main__":
    main()
