import socket, json, pygame


clock = pygame.time.Clock()

IP = socket.gethostbyname(socket.gethostname())
PORT = 6767

info = {
    "connection": "not established"
}

ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()

connection, addr = server.accept()

def receive_msg():
    global info
    info = json.loads(connection.recv(1024).decode("utf-8"))

while True: 
    receive_msg() 


    print(info["connection"])

    if info["connection"] == "established":
        connection.send("connection established".encode("utf-8"))

    clock.tick(1)

    



    