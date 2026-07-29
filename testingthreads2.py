import socket, threading

PORT = 7676
IP = socket.gethostbyname(socket.gethostname())

ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDR)
    client.send("connected".encode("utf-8"))
except:
    print("error while connecting")