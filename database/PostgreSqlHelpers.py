############################################################
#PostgreSqlHelpers is class suport for connectting with postgre SQL
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
#Link: https://github.com/thanhntt89/python-projects/blob/main/database/PostgreSqlHelpers.py
#Created date: 2021/08/08
############################################################
import os
import psycopg2 as psycop
import pandas as pd
from configparser import ConfigParser

class PostgreSqlHelpers():
   
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
    connection =''
    @staticmethod
    def GetConnectionString():
        PostgreSqlHelpers.connection_string = f"host='{PostgreSqlHelpers.SERVER}' dbname='{PostgreSqlHelpers.DATABASE}' user='{PostgreSqlHelpers.USER_NAME}' password='{PostgreSqlHelpers.PASSWORDS}' port='{PostgreSqlHelpers.PORT}'"
        return PostgreSqlHelpers.connection_string

    @staticmethod
    def GetConnection():
        return psycop.connect(PostgreSqlHelpers.GetConnectionString())
        #return psycop.connect(database=PostgreSqlHelpers.DATABASE, user=PostgreSqlHelpers.USER_NAME, password=PostgreSqlHelpers.PASSWORDS, host=PostgreSqlHelpers.SERVER, port=PostgreSqlHelpers.PORT)

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
    
    #Create transaction object
    @staticmethod
    def CreateTransaction(connection_string):
        try:
            PostgreSqlHelpers.connection = psycop.connect(connection_string)
            PostgreSqlHelpers.connection.autocommit = False
            #con.timeout = PostgreSqlHelpers.COMMAND_TIMEOUT     
            PostgreSqlHelpers.transaction = PostgreSqlHelpers.connection.cursor()           
        except ValueError as e:
            raise e.args

    ################################################################
    #Add query to transaction
    ################################################################
    @staticmethod
    def TransactionAdd(query):
        PostgreSqlHelpers.transaction.execute(query)

    ################################
    #Add query to transaction with parameters
    ################################
    @staticmethod
    def TransactionAddWithParameters(query, parameters):
        PostgreSqlHelpers.transaction.execute(query, parameters)

    ################################################################
    #Transaction committing to database
    ################################################################
    @staticmethod
    def TransactionCommitting():
        try:
            PostgreSqlHelpers.connection.commit()    
            PostgreSqlHelpers.connection.close()    
        except ValueError as e:
            PostgreSqlHelpers.connection.rollback() 
            PostgreSqlHelpers.connection.close() 
            raise e.args  

   
    ################################################################
    #Get data in table from database
    #Return dict data
    ################################################################
    @staticmethod
    def ExecuteDict(connection_string, query):
        try: 
            connection = psycop.connect(connection_string)
            cur = connection.cursor()   
            cur.execute(query) 
            dat_row = cur.fetchall()
            columns = [cols[0] for cols in cur.description] 
            data = [dict(zip(columns, row)) for row in dat_row]
            connection.close()
            return data 
        except Exception as e:
            connection.close()
            raise e.args

    @staticmethod
    def ExecuteDataFrame(connection_string, query):
        try:    
            connection = psycop.connect(connection_string)
            data = pd.read_sql_query(query,connection)
            connection.close()         
            return data
        except Exception as e: 
            connection.close()           
            raise e.args

    ###############################
    # SQL running with query parameter character ? and values array
    ###############################
    @staticmethod
    def ExecuteNonQueryWithParameters(connection_string, query,vales):
        try:              
            connection = psycop.connect(connection_string)
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
    def ExecuteNonQuery(connection_string, query):
        try:     
            connection = psycop.connect(connection_string)
            cur = connection.cursor()             
            cur.execute(query)    
            connection.commit() 
            connection.close()
        except ValueError as e:            
            connection.rollback()
            connection.close()
            raise e.__traceback__

    #########################
    #Load file config file
    #Info config file:
    #Line 1: [POSTGRECONFIG]
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

            PostgreSqlHelpers.SERVER = config.get('POSTGRECONFIG','SERVER')
            PostgreSqlHelpers.USER_NAME = config.get('POSTGRECONFIG','USER_NAME')
            PostgreSqlHelpers.PASSWORDS = config.get('POSTGRECONFIG','PASSWORD')
            PostgreSqlHelpers.DATABASE = config.get('POSTGRECONFIG','DATABASE')
            PostgreSqlHelpers.COMMAND_TIMEOUT = int(config.get('POSTGRECONFIG','COMMAND_TIMEOUT')) 
            PostgreSqlHelpers.CONNECTION_TIMEOUT = int(config.get('POSTGRECONFIG','CONNECTION_TIMEOUT'))
            PostgreSqlHelpers.PORT = int(config.get('POSTGRECONFIG','PORT'))
        except ValueError as e:
            raise e.args
        
def main():
    #test 
    FILE_NAME= 'sqlconfig.txt'
    file_path = os.path.join(os.path.dirname(__file__),FILE_NAME) 
    PostgreSqlHelpers.LoadingFileConfig(file_path)

    #print('connection_string:'+ PostgreSqlHelpers.GetConnectionString())
    connection_string = PostgreSqlHelpers.GetConnectionString()
    #print('Connection string:'+str(PostgreSqlHelpers.test_connection(connection)))
    #Test execute_non_query
    #Test_ExecuteNonQuery(connection_string)
    #Test_ExecuteNonQueryWithParameter(connection_string)
    #Test_ExecuteTransaction(connection_string)
    #Tes_ExecuteDick(connection_string)
    Test_ExecuteDataFrame(connection_string)


def Test_ExecuteDataFrame(connection_string):
    query ='select * from member'
    print(PostgreSqlHelpers.ExecuteDataFrame(connection_string, query))

def Tes_ExecuteDick(connection_string):
    #query ='create table test(id serial primary key, name varchar(255))'
    query ='select * from member'
    data =  PostgreSqlHelpers.ExecuteDict(connection_string,query)
    print(data)

def Test_ExecuteNonQuery(connection_string):
    #query = "INSERT INTO test (id, name) VALUES(2,'Ngay khong em')"   
    query = 'insert into member (username,fullname,email) values({0},{1},{2})'.format("'jimmii88'","'Nguyen Tat Thanh'","'thanhntt89bk@gmail.com'")  
    #using dictionnary

    #print(query)
    PostgreSqlHelpers.ExecuteNonQuery(connection_string, query)

def Test_ExecuteNonQueryWithParameter(connection_string):  
    query ='insert into member (username,fullname,email) values(%s,%s,%s)'
    parameters =('admin','Nguyen Tat Thanh','thanhntt89@yahoo.com')
    PostgreSqlHelpers.ExecuteNonQueryWithParameters(connection_string, query,parameters)

def Test_ExecuteTransaction(connection_string):
    query = "INSERT INTO member (username,fullname,email) values('supperadmin','Administrator','admin@gmail.com')"
    query0 = 'insert into member (username,fullname,email) values({0},{1},{2})'.format("'jimmii88'","'Nguyen Tat Thanh'","'thanhntt89bk@gmail.com'")  
    query1 ='insert into member (username,fullname,email) values(%s,%s,%s)'
    parameters =('admin','Nguyen Tat Thanh','thanhntt89@yahoo.com')

    PostgreSqlHelpers.CreateTransaction(connection_string)
    PostgreSqlHelpers.TransactionAdd(query)
    PostgreSqlHelpers.TransactionAdd(query0)
    PostgreSqlHelpers.TransactionAddWithParameters(query1, parameters)
    PostgreSqlHelpers.TransactionCommitting()
if __name__ == '__main__':
    main()