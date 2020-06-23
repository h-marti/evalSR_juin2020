#!/usr/bin/python3

import socket

class Client(object):

    userPrompt = ""
    
    def __init__(self) :
        # Création de la socket IPv4 (AF_INET) en TCP (SOCK_STREAM)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connexion au serveur 127.0.0.1 sur le port TCP/6969
        self.sock.connect(("127.0.0.1", 6969))

    def EnvoieVersServeur(self, userPrompt) :
        # Envoi de données au serveur
        nb_bytes = self.sock.send(userPrompt.encode(encoding='UTF-8',errors='ingnore'))
        print("[INFO] sent %d bytes to server" % nb_bytes)

    def ReceptionReponse(self) :
        # Réception de données du serveur
        data = self.sock.recv(1024) # 8192 = nombre d'octets maximal à lire
        data_ascii = data.decode("ascii") # les données sont de type "byte" il faut les décoder pour afficher
        
        return "[INFO] received from data from server : %s" % data_ascii

    def __del__(self) :
        # Fermeture de la socket
        self.sock.close()