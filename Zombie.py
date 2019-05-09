import socket
import threading
from threadsPourZombie import thread_recevoir
server_ip = "192.168.60.113"  # ip du serveur
server_port = 89  # port du serveur

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
thread_recevoir = threading.Thread(target=thread_recevoir, args={client, })
print("connecter")
thread_recevoir.start()

while True:  # print le texte recu
    texte = input(" ")
    client.send(str.encode(texte))
