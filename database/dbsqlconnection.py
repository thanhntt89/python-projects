import pyodbc as odbc

class dbsqlconnection():
    SERVER = 'WINSERVER2016'
    USER_NAME='wiiAdmin'
    PASSWORDS='W_iiAdmin00000'
    DATABASE ='Wii'
    connection_string = ''
    
    @classmethod
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER='+self.SERVER+';DATABASE='+self.DATABASE+';UID='+self.USER_NAME+';PWD='+ self.PASSWORDS
   
    @classmethod
    def getConnectionString(self):
        return self.connection_string

    @classmethod
    def test_connection(self):
        #('ConnectionString:'+ self.connection_string)
        try:            
            con = odbc.connect(self.connection_string)
            cur = con.cursor()
            query ="SELECT @@version;"
            cur.execute(query) 
            # row = cur.fetchone()        
            # while row: 
            #     print(row[0])
            #     row = cur.fetchone()
            return True
        except:
            return False
 
def main():
    db = dbsqlconnection()
    #print(db.getConnectionString())
    print('Connected:'+  str(db.test_connection()))

if __name__ =='__main__':
    main()