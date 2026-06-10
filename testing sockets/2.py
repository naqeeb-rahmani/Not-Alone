import socket, json, pygame

clock = pygame.time.Clock()

IP = socket.gethostbyname(socket.gethostname())
PORT = 6767

ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



#connection, port = client.accept()

info = {
    "connection": "established"
}


msg = json.dumps(info)

while True:

    client.send(msg.encode("utf-8"))

    print(client.recv(1024).decode("utf-8"))


    clock.tick(1)


'''while True:
    received_msg = client.recv(1024)
    if len(received_msg) > 0:
        print(received_msg)'''

