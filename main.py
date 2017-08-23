import queue

from worker import Worker
from sender import Sender
from receiver import Receiver

if __name__ == '__main__':
    
    in_qs = list()
    out_qs = list()

    worker_threads = list()
    sender_threads = list()

    n = 4
    for i in range(n):
        in_q = queue.Queue()
        out_q = queue.Queue()
        
        in_qs.append(in_q)
        out_qs.append(out_q)

        worker = Worker(i, in_q, out_q)
        worker_threads.append(worker)

        reply_target = ('127.0.0.1', 9000)
        sender = Sender(i, out_q, reply_target)
        sender_threads.append(sender)

    recv_netinfo = ('127.0.0.1', 8000)
    recv_thread = Receiver(in_qs, n, recv_netinfo)

    for i in range(n):
        worker_threads[i].start()
        sender_threads[i].start()

    recv_thread.start()



    
