import pyodbc as odbc

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
    @staticmethod
    def ExecuteDataset(connection_string,query):
        con = odbc.connect(connection_string)
        con.timeout = SqlHelpers.COMMAND_TIMEOUT
        cur = con.cursor()        
        cur.execute(query) 
        dat_row = cur.fetchall()
        columns = [cols[0] for cols in cur.description]
        return columns,dat_row

             

def main():
    SqlHelpers.SERVER ='WINSERVER2016'
    SqlHelpers.DATABASE ='Wii'
    SqlHelpers.PASSWORDS ='W_iiAdmin00000' 
    SqlHelpers.USER_NAME ='wiiAdmin'

    connection_string = SqlHelpers.GetConnectionString()

    print('Sql connection string :'+ connection_string)

    print('Test connected:' + str(SqlHelpers.test_connection(connection_string)))

    #query = 'select [利用者ID],[権限グループ],[利用者名] from  [Wii].[dbo].[Fes利用者]'
    query = 'EXEC [dbo].[select_test]'
    columns , user_group_dataset = SqlHelpers.ExecuteDataset(connection_string, query)

    print('User_groups:\n')
    print(columns)
    #print(user_group)
    for ug in user_group_dataset:
        print(ug)

if __name__ == "__main__":
    main()
