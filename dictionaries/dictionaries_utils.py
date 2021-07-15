class dictionariesUtils():
    MY_DICTIONS = {}

    def create_dict(self):
        return self.MY_DICTIONS

    def addToDict(self,key:str,value):
        self.MY_DICTIONS[key]= value

    def getFieldByKey(self, key:str):
        try:
            return self.MY_DICTIONS[key]
        except KeyError as e:
            return f'error key {e}'

def main():
    _dict = dictionariesUtils()
    _dict.addToDict("city","Ha Noi")
    _dict.addToDict("popular",8)

    my_dict = _dict.create_dict()
    
    print(f'dict: {my_dict}')  
    print(f'get values by key = city :{_dict.getFieldByKey("city")}')

    #add new key and values
    _dict.addToDict("leader","Nguyen Tat Thanh")
    print(f'after add values: {_dict.MY_DICTIONS}')

if __name__ == '__main__':
    main()