import json
from pprint import pprint
import socket

# program crashed but linux still reserved port 65432
# to release port 65432:
# sudo fuser -k 65432/tcp

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)

while True:
    print("Waiting for connection...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                msg = {"message": "Hello World"}
                msg = json.dumps(msg).encode("utf-8")
                conn.sendall(msg)

                ack = conn.recv(1024)
                if not ack:
                    break
