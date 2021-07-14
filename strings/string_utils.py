class stringUtils():  
    @classmethod
    def getUserAndDomain(self,email):
        user_name = email[0:email.index("@")]
        domain_name = email[email.index("@")+1:]  
        return [user_name, domain_name]

    @classmethod
    def printMsg(self,user_name, domain_name):
        print(f'user_name:{user_name}\ndomain_name:{domain_name}')

    @staticmethod
    def getSubString(val,startIndex,endIndex):
        result = val[startIndex:endIndex]
        return result
    
    @staticmethod
    def reverseString(val):
        return val[::-1]
    
    @staticmethod
    def takeEveryPosition(val, position):
        return val[::position]

    @staticmethod
    def joinStringArrayByChar(val):
        return ' '.join(val)

    @staticmethod
    def checkCharInString(val,char):
        if char in val:
            return True
        else:
            return False

    @staticmethod
    def convertStringToArray(val,split_char):
        return val.split(split_char)
    
    @staticmethod
    def convertStringToArray(val):
        return val.split()
    
    @staticmethod
    def countCharInString(val,char_count):
        return val.count(char_count)
        
def main():    
    sbstr = string_utils()
    email = input("Please input email:").strip()        
    user_name, domain_name = sbstr.getUserAndDomain(email)
    sbstr.printMsg(user_name, domain_name)

if __name__ == "__main__":
        main()

