from threading import Thread
import time

def timer(name, delay, counter):
    print("timer :" + name + "started \n")

    while counter > 0:
        time.sleep(delay)
        print(name + ":" + str(time.ctime(time.time())))
        counter -= 1
    print("timer : " + name + " completed \n" )
def Main():
    t1 = Thread(target = timer, args = ("timer 1", 5, 5))
    t2 = Thread(target = timer, args = ("timer 2", 3, 5))

    t1.start()
    t2.start()

    print("Main function completed \n")

if __name__ == '__main__':
    Main()

                
    
    
