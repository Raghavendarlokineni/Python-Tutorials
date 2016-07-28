from queue import Queue

"""
queue maxsize is by default infinite. It can be modified as below.
"""
q = Queue(maxsize = 4)

print("------Queue info when putting -----")

for i in range(5):

    print("---Loop---- :", i) 
    print("queue empty : ", q.empty())

    """
    we have defines queue's max size is 4. Hence it runs successfully for 4 iterations.
    During the fifth iteration, the queue has already 4 tasks in it and waits for TIMEOUT
    time and throws an error QUEUE.FULL. TRY block will handle when the queue is full.
    """
    try :
        q.put(i, timeout = 10)
    except :
        print("queue size is fill, max value is ", q.maxsize)
        break
        
    print("queue size : ", q.qsize())
    
    print("queue full : ", q.full())

print("------Queue info when getting -----")        

for i in range(q.maxsize): 

    print("---Loop---- :",i)
    print("get : ", q.get(i, timeout = 10))
    print("task done : ", q.task_done())
    print("queue empty : ", q.empty())
    

