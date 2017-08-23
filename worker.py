import threading
import hashlib
import random

class Worker(threading.Thread):
    def __init__(self, w_id, in_q, out_q):
        threading.Thread.__init__(self)
        self.id = w_id
        self.in_q = in_q
        self.out_q = out_q
        self.hasher = hashlib.sha512()

    def process(self, imsg):
        msgclient = imsg['client']
        msgid = imsg['id']
        msgtxt = imsg['text'] #str
        
        msgencode = str.encode(msgtxt)
        self.hasher.update(msgencode)
        msghash = self.hasher.hexdigest()
        print(self.id) #, msgclient, msgid, msgtxt, msghash)

        rounds = random.randint(100, 1000)
        for i in range(rounds):
            self.hasher.update(str.encode(msghash))
            msghash = self.hasher.hexdigest()
        
        omsg = dict()
        omsg['client'] = msgclient
        omsg['id'] = msgid
        omsg['rounds'] = rounds
        omsg['hash'] = msghash
        omsg['worker'] = self.id
        return omsg

    def run(self):
        while True:
            msg = self.in_q.get(True)
            result = self.process(msg)
            self.out_q.put(result)