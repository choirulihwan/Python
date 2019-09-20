import _thread
import time

def CounterDown(ThreadName):
    count = 10
    while(count > 0):
        print("{}, Count:{} ".format(ThreadName, count))
        count -= 1
        time.sleep(1)

def main():
    try:
        _thread.start_new_thread(CounterDown,("Thread1",))
        print("Thread end")
        #_thread.start_new_thread(CounterDown,("Thread2",))
    except:
        print("Unable to start thread")
    while 1:
        pass


if __name__ == '__main__': main()
