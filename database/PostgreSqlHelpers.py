############################################################
#SqlHelpers is class suport for connectting with postgre SQL
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
#Link: https://github.com/thanhntt89/python-projects/blob/main/database/PostgreSqlHelper.py
#Created date: 2021/08/08
############################################################
import os
import psycopg2 as psycopg2
import pandas as pd
from configparser import ConfigParser

class PostgreSqlHelper():
    def __init__(self) -> None:
        pass

     #Default connection information
    HOST = ''
    USER_NAME = ''
    PASSWORDS = ''
    DATABASE = ''
    #Time out execute query 
    COMMAND_TIMEOUT = 5000
    #Time out check connection
    CONNECTION_TIMEOUT = 300

    #Default connection string
    connection_string = 'HOST='+HOST+';DATABASE='+DATABASE+';USER='+USER_NAME+';PASSWORD='+ PASSWORDS
    
    #transaction variable
    transaction = ''

    #Create transaction object
    @staticmethod
    def CreateTransaction(connection_string):
        try:
            con = psycopg2.connect(connection_string, autocommit=False)
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
    
    #########################
    #Create connection string
    #########################
    @staticmethod
    def GetConnectionString():
        PostgreSqlHelper.connection_string = 'SERVER='+PostgreSqlHelper.HOST+';DATABASE='+PostgreSqlHelper.DATABASE+';UID='+PostgreSqlHelper.USER_NAME+';PWD='+ PostgreSqlHelper.PASSWORDS 
        return PostgreSqlHelper.connection_string

    @staticmethod
    def test_connection(connection_string):        
        try:            
            con = psycopg2.connect(connection_string)
            con.timeout = PostgreSqlHelper.CONNECTION_TIMEOUT
            cur = con.cursor()
            cur.open()  
            cur.closest()
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
            con = psycopg2.connect(connection_string)
            con.timeout = PostgreSqlHelper.COMMAND_TIMEOUT
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
            con = psycopg2.connect(connection_string)
            con.timeout = PostgreSqlHelper.COMMAND_TIMEOUT
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
            con = psycopg2.connect(connection_string)
            con.timeout = PostgreSqlHelper.COMMAND_TIMEOUT           
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
            con = psycopg2.connect(connection_string, autocommit = True)
            con.timeout = PostgreSqlHelper.COMMAND_TIMEOUT           
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

            PostgreSqlHelper.HOST = config.get('POSTGRECONFIG','HOST')
            PostgreSqlHelper.USER_NAME = config.get('POSTGRECONFIG','USER_NAME')
            PostgreSqlHelper.PASSWORDS = config.get('POSTGRECONFIG','PASSWORD')
            PostgreSqlHelper.DATABASE = config.get('POSTGRECONFIG','DATABASE')
            PostgreSqlHelper.COMMAND_TIMEOUT = int(config.get('POSTGRECONFIG','COMMAND_TIMEOUT')) 
            PostgreSqlHelper.CONNECTION_TIMEOUT = int(config.get('POSTGRECONFIG','CONNECTION_TIMEOUT'))
        except ValueError as e:
            raise e.args