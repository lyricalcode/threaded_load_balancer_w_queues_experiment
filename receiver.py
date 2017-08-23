import threading
import socket
import json

MAX_SIZE = 1024

class Receiver(threading.Thread):
    def __init__(self, in_qs, num_threads, netinfo):
        threading.Thread.__init__(self)
        self.in_qs = in_qs
        self.num_threads = num_threads
        self.netinfo = netinfo #(ip, port)
        self.in_socket = None

    def run(self):
        self.in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.in_socket.bind(self.netinfo)

        counter = 0
        while True:
            msg = self.in_socket.recv(MAX_SIZE)
            msg = msg.decode()
            msg = json.loads(msg)

            worker = counter % self.num_threads 
            self.in_qs[worker].put(msg)

            #print(worker)
            counter = worker + 1