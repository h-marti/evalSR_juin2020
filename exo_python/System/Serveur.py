#!/usr/bin/python3

import socket
import threading

class Serveur(object):

	# Création de la socket TCP en IPv4
	__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	__client_sock = ""
	__client_data = ""
	__threads = []

	def __init__(self) :
		print("[SRV] Construction")

		# Permet d'éviter l'erreur "address already in use"
		# quand on relance plusieurs fois le serveur
		self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		# En écoute sur 0.0.0.0:6969
		self.__sock.bind(("0.0.0.0", 6969))

		# Lancer l'écoute avec au maximum 8 clients
		self.__sock.listen(8)

	def ReceptionMessage(self) :

		############################################################################################
		#TODO : Threading
		############################################################################################

		def Reception(self, client_addr) :
			# Lire les données du client (maximum 8192 octets)
			self.__client_data = self.__client_sock.recv(1024)
			print("[INFO] %s a envoyé : %s" % (client_addr[0], self.__client_data))

			return self.__client_data

		print("[SRV] Reception")
		
		# Accepter une connexion
		(self.__client_sock, client_addr) = self.__sock.accept()
		print("[INFO] %s est connecté" % client_addr[0])
		
		t = threading.Thread(target=Reception, args=(client_addr))
		threads.append(t)
		

	def EnvoieVersClient(self) :
		print("[SRV] Envoie")
		
		# Envoyer des données au client
		self.__client_sock.sendall(b"[Reception] : " + self.__client_data)
		# Fermer la connexion avec le client
		self.__client_sock.close()

	def __del__(self) :
		print("[SRV] Destruction")

		# Fermeture de la socket
		self.__sock.close()