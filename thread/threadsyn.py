import time
import threading
class Account:
    def __init__(self, name, accountTotal):
        self.name = name
        self.accountTotal = accountTotal
    locked = threading.Lock()

    def withDraw(self,username, account, amount):   
        print('Thread:'+ username)
        self.locked.acquire()
        while True:
        
            if(account.accountTotal >= amount):
                account.accountTotal -= amount
                print("username: "+username+" Account: "+account.name+ "Balance:"+str(account.accountTotal))
            else:
                print("Account: "+account.name+ "Balance is zero:"+str(account.accountTotal))
            if account.accountTotal <= 0:
                break
            time.sleep(0.5)
        self.locked.release()

    array =[1,2,3,4,5,6,7,8,9]

    def __str__(self):
        return ','.join( [str(a) for a in self.array])

def main():
    a = Account('Account1', 100000)   
    t1 = threading.Thread(target= a.withDraw,args=("a1",a,1000))
    t2 = threading.Thread(target= a.withDraw,args=("a2",a, 500))
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()