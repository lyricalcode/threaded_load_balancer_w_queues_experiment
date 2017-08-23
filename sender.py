import threading
import socket
import json

class Sender(threading.Thread):
    def __init__(self, s_id, out_q, target):
        threading.Thread.__init__(self)
        self.id = s_id
        self.out_q = out_q
        self.target = target # (ip, port)

    def run(self):

        while True:
            msg = self.out_q.get(True)
            msgjson = json.dumps(msg)
            msgstr = str.encode(msgjson)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(msgstr, self.target)

