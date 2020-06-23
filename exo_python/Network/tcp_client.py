#!/usr/bin/python3

import socket

userPrompt = ""

while userPrompt != "quit":

    # Création de la socket IPv4 (AF_INET) en TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur 127.0.0.1 sur le port TCP/6969
    sock.connect(("127.0.0.1", 6969))
    
    userPrompt = input("> ")

    # Envoi de données au serveur
    nb_bytes = sock.send(userPrompt.encode(encoding='UTF-8',errors='ingnore'))
    print("[INFO] sent %d bytes to server" % nb_bytes)

    # Réception de données du serveur
    data = sock.recv(1024) # 8192 = nombre d'octets maximal à lire
    data_ascii = data.decode("ascii") # les données sont de type "byte" il faut les décoder pour afficher
    print("[INFO] received from data from server : %s" % data_ascii)

    # Fermeture de la socket
    sock.close()