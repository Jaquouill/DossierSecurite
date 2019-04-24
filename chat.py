import socket
import threading

server_ip = "127.0.0.1"
server_port = 9999


def thread_recevoir(client_socket):
    while True:
        response = client.recv(1024)
        print(response)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
thread_recevoir = threading.Thread(target=thread_recevoir, args={client, })
thread_recevoir.start()
while True:
    texte = input("your text:")
    client.send(str.encode(texte))
