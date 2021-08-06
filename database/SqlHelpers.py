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
            con.timeout = SqlHelpers.COMMAND_TIMEOUT
            cur = con.cursor()            
            query ="SELECT @@version;"
            cur.execute(query)            
            return True
        except:
            return False
    
    #Get data in table from database
    @staticmethod
    def ExecuteDataset(connection_string,query):
        con = odbc.connect(connection_string)
        con.timeout = SqlHelpers.COMMAND_TIMEOUT
        cur = con.cursor()
        cur.execute(query)  
        return cur.fetchall() 

             

def main():
    SqlHelpers.SERVER ='WINSERVER2016'
    SqlHelpers.DATABASE ='WiiTmp'
    SqlHelpers.PASSWORDS ='W_iiAdmin00000' 
    SqlHelpers.USER_NAME ='wiiAdmin'

    #print('Sql connection string :'+ SqlHelpers.connection_string)

    #print('Test connected:' + str(SqlHelpers.test_connection()))

    #query = 'select [利用者ID],[権限グループ],[利用者名] from  [Wii].[dbo].[Fes利用者]'
    query = 'EXEC [dbo].[select_test]'
    user_group_dataset = SqlHelpers.ExecuteDataset(SqlHelpers.connection_string, query)
    print('User_groups:\n')
    #print(user_group)
    for ug in user_group_dataset:
        print(ug)

if __name__ == "__main__":
    main()
