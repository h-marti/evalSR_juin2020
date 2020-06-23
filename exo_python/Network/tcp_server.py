#!/usr/bin/python3

import socket

# Création de la socket TCP en IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Permet d'éviter l'erreur "address already in use"
# quand on relance plusieurs fois le serveur
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# En écoute sur 0.0.0.0:6969
sock.bind(("0.0.0.0", 6969))

# Lancer l'écoute avec au maximum 16 clients
sock.listen(8)

# Le serveur tourne indéfiniment
while True :
	# Accepter une connexion
	(client_sock, client_addr) = sock.accept()
	print("[INFO] %s est connecté" % client_addr[0])
	# Lire les données du client (maximum 8192 octets)
	client_data = client_sock.recv(1024)
	print("[INFO] %s a envoyé : %s" % (client_addr[0], client_data))
	# Envoyer des données au client
	client_sock.sendall(b"[Reception] : " + client_data)
	# Fermer la connexion avec le client
	client_sock.close()

# Fermeture de la socket
sock.close()