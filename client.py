import socket
import json
import random
import string
import sys

client = int(sys.argv[1])

server_netinfo = ('127.0.0.1', 8000)

counter = 0
while True:
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = dict()
    msg['client'] = client
    msg['id'] = counter
    # 10 char random strings
    msg['text'] = ''.join(random.SystemRandom().choices(string.ascii_uppercase + string.digits, k=random.randint(10,900)))

    msgjson = json.dumps(msg)
    msgstr = str.encode(msgjson)

    send_sock.sendto(msgstr, server_netinfo)
    counter += 1

    if counter == 10000:
        break
