"""
connect and bind to a socket
send data to the socket
"""

from pprint import pprint
import socket
import json
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        now = time.time()
        data = s.recv(1024)
        decoded = json.loads(data.decode("utf-8"))

        pprint(decoded)
        s.sendall(b"ack")
        # print time taken in millis
        print(time.time() - now)
