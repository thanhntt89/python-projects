import threading 
import time

class threadutils(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print('run threading name: '+ self.name)       
        while self.counter:
            time.sleep(self.delay)
            print('%s:%s' % (self.name, time.ctime(time.time())))
            self.counter -= 1
        print('Finished running threading name: '+ self.name)
   

def main():
    threads = []
    thread1 = threadutils('Thread 1',10,3)
    thread2 = threadutils('Thread 2',20,1)    

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for thread in threads:
        thread1.join()
    print('Finished all threads')

if __name__ == '__main__':
    main()