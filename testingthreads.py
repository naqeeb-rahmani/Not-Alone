import socket, threading, os

PORT = 7676
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen()

break_loop = False

def connect():
    global break_loop
    connection, port = server.accept()
    message = connection.recv(1024).decode("utf-8")

    if message == "connected":
        break_loop = True
    
    else:
        break_loop = False
    



threading.Thread(target=connect).start()

while True:
    os.system('cls')

    if break_loop:
        break
    else:
        print("waiting for connection")

    
    
        

