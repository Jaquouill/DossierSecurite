import socket
import threading

# tableau de clients
tb_client = []
# addresse ip du server
bind_ip = "192.168.60.113"
# num de port du server
bind_port = 89

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
server.bind((bind_ip, bind_port))
# le serveur attend une réponse des clients ou une connection
server.listen(5)
#
print("Le serveur est en attente...")


# fonction qui envoie une requête aux clients
def thread_recevoir_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        print(" \n Received: %s" % request)


#
def thread_connection():
    while True:

        client, addr = server.accept()
        tb_client.append([client])

        #
        for i in range(tb_client.__len__()):
            print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))
            trc = threading.Thread(target=thread_recevoir_client, args={client, })
            trc.start()
            thread_recevoir_client()
            tb_client[i].send(str.encode(texte))


thread_connection()
while True:
    text = texte.split(" ")
    texte = input(" \n text: ")



