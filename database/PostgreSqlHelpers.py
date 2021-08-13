############################################################
#PostgreSqlHelper is class suport for connectting with postgre SQL
#Supported with transaction, return pandas object, dict object 
#Support reading connection info from files config 
#File config example: 
#[POSTGRECONFIG]
#HOST = SERVER
#USER_NAME = USER_NAME
#PASSWORD = PASSWORD
#CONNECTION_TIMEOUT =CONNECTION_TIMEOUT
#COMMAND_TIMEOUT = COMMAND_TIMEOUT
############################################################
#Created by: Nguyen Tat Thanh (Jimmii88)
#Email: thanhntt89bk@gmail.com
#Link: https://github.com/thanhntt89/python-projects/blob/main/database/PostgreSqlHelper.py
#Created date: 2021/08/08
############################################################
import os
import psycopg2 as psycop
import pandas as pd
from configparser import ConfigParser

class PostgreSqlHelper():
   
     #Default connection information
    SERVER = ''
    USER_NAME = ''
    PASSWORDS = ''
    DATABASE = ''
    PORT = 5432
    #Time out execute query 
    COMMAND_TIMEOUT = 5000
    #Time out check connection
    CONNECTION_TIMEOUT = 300

    #Default connection string
    connection_string = ''
    
    #transaction variable
    transaction = ''

    #Create transaction object
    @staticmethod
    def CreateTransaction(connection_string):
        try:
            con = psycop.connect(connection_string, autocommit=False)
            con.timeout = PostgreSqlHelper.COMMAND_TIMEOUT     
            PostgreSqlHelper.transaction = con.cursor()           
        except ValueError as e:
            raise e.args

    ################################################################
    #Add query to transaction
    ################################################################
    @staticmethod
    def TransactionAdd(query):
        PostgreSqlHelper.transaction.execute(query)

    ################################
    #Add query to transaction with parameters
    ################################
    @staticmethod
    def TransactionAddWithParameters(query, parameters):
        PostgreSqlHelper.transaction.execute(query, parameters)

    ################################################################
    #Transaction committing to database
    ################################################################
    @staticmethod
    def TransactionCommitting():
        try:
            PostgreSqlHelper.transaction.commit()       
        except ValueError as e:
            PostgreSqlHelper.transaction.rollback() 
            raise e.args  

    @staticmethod
    def GetConnection():
        return psycop.connect(database=PostgreSqlHelper.DATABASE, user=PostgreSqlHelper.USER_NAME, password=PostgreSqlHelper.PASSWORDS, host=PostgreSqlHelper.SERVER, port=PostgreSqlHelper.PORT)

    @staticmethod
    def test_connection(connection):        
        try:   
            cur = connection.cursor()
            cur.execute('select version()')  
            print(cur.fetchone())          
            return True
        except ValueError as e:
            e.__traceback__
            return False
    
    ################################################################
    #Get data in table from database
    #Return dict data
    ################################################################
    @staticmethod
    def ExecuteDict(con, query):
        try:           
            cur = con.cursor()        
            cur.execute(query) 
            dat_row = cur.fetchall()
            columns = [cols[0] for cols in cur.description] 
            data = [dict(zip(columns, row)) for row in dat_row]
            return data 
        except Exception as e:
            raise e.args

    @staticmethod
    def ExecuteDataFrame(connection, query):
        try:    
            data = pd.read_sql_query(query,connection)
            return data
        except Exception as e:            
            raise e.args

    ###############################
    # SQL running with query parameter character ? and values array
    ###############################
    @staticmethod
    def ExecuteNonQueryWithParameters(connection, query,vales):
        try:              
            #connection = PostgreSqlHelper.GetConnection()        
            cur = connection.cursor() 
            cur.execute(query, vales)   
            connection.commit() 
            connection.close()
        except ValueError as e:
            connection.rollback()
            connection.close()
            raise e.__traceback__

    #########################
    # SQL running query without parameters
    #########################
    @staticmethod
    def ExecuteNonQuery(connection, query):
        try:                       
            cur = connection.cursor() 
            cur.execute(query,vars=None)    
            connection.commit() 
            connection.close()
        except ValueError as e:            
            connection.rollback()
            connection.close()
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

            PostgreSqlHelper.SERVER = config.get('POSTGRECONFIG','SERVER')
            PostgreSqlHelper.USER_NAME = config.get('POSTGRECONFIG','USER_NAME')
            PostgreSqlHelper.PASSWORDS = config.get('POSTGRECONFIG','PASSWORD')
            PostgreSqlHelper.DATABASE = config.get('POSTGRECONFIG','DATABASE')
            PostgreSqlHelper.COMMAND_TIMEOUT = int(config.get('POSTGRECONFIG','COMMAND_TIMEOUT')) 
            PostgreSqlHelper.CONNECTION_TIMEOUT = int(config.get('POSTGRECONFIG','CONNECTION_TIMEOUT'))
            PostgreSqlHelper.PORT = int(config.get('POSTGRECONFIG','PORT'))
        except ValueError as e:
            raise e.args
        
def main():
    #test 
    FILE_NAME= 'sqlconfig.txt'
    file_path = os.path.join(os.path.dirname(__file__),FILE_NAME) 
    PostgreSqlHelper.LoadingFileConfig(file_path)
    print('Connection string:'+str(PostgreSqlHelper.test_connection(PostgreSqlHelper.GetConnection())))
    #Test execute_non_query
    Test_ExecuteNonQuery(PostgreSqlHelper.GetConnection())

def Test_ExecuteNonQuery(connection):
    query = "INSERT INTO (User) (UserName, UserId, Email, FullName) VALUES (%s,%s,%s,%s)"
    parameters =(U'jimmii88',2,U'thanhntt89bk@gmail.com',U'Nguyen Tat Thanh')
    postgres_insert_query = """ INSERT INTO %s (ID, MODEL, PRICE) VALUES (%s,%s,%s)""",U"mobile"
    record_to_insert = (5, U'One Plus 6', 950)

    columns = ["ID","Model","PRICE"]
    values = [5,'One Plus 6',960]
    query1= "insert into mobile (%s) values (%s)",','.join(columns)#,','.join(values)
    print ("query1: "+ query1)
    
    # cursor = connection.cursor()
    # cursor.execute(query1)
    # connection.commit()
    # count = cursor.rowcount
    # #query = """INSERT INTO User (UserName, UserId, Email, FullName) VALUES (%s,%s,%s,%s);""", {'jimmii88','2','thanhntt89bk@gmail.com','Nguyen Tat Thanh',}
    # PostgreSqlHelper.ExecuteNonQuery(connection, query)
    #PostgreSqlHelper.ExecuteNonQueryWithParameters(connection, query,parameters)
    

if __name__ == '__main__':
    main()