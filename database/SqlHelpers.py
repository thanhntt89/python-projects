import pyodbc as odbc

class SqlHelpers():
    #Default connection information
    SERVER = 'WINSERVER2016'
    USER_NAME='wiiAdmin'
    PASSWORDS='W_iiAdmin00000'
    DATABASE ='Wii'
    COMMAND_TIMEOUT = 5000

    connection_string = 'DRIVER={SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER_NAME+';PWD='+ PASSWORDS
    
    @staticmethod
    def test_connection():        
        try:            
            con = odbc.connect(SqlHelpers.connection_string)
            cur = con.cursor()
            query ="SELECT @@version;"
            cur.execute(query)            
            return True
        except:
            return False
    
    @staticmethod
    def ExecuteNonQuery(connection_string,query):
        con = odbc.connect(connection_string)
        cur = con.cursor()
        cur.execute(query)            

def main():
    SqlHelpers.SERVER ='WINSERVER2016'
    SqlHelpers.DATABASE ='WiiTmp'
    SqlHelpers.PASSWORDS ='W_iiAdmin00000' 
    SqlHelpers.USER_NAME ='wiiAdmin'

    print('Sql connection string :'+ SqlHelpers.connection_string)

    print('Test connected:' + str(SqlHelpers.test_connection()))

if __name__ == "__main__":
    main()
