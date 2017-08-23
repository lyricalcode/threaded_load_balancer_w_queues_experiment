import socket
import json

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(('127.0.0.1', 9000))

while True:
    msg = recv_sock.recv(1024)
    msg = msg.decode()
    msg = json.loads(msg)
    print(msg)