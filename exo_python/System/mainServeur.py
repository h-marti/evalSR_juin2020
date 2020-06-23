#!/usr/bin/python3

from Serveur import Serveur

MyServeur = Serveur()

while True :
    client_Data = MyServeur.ReceptionMessage()
    MyServeur.EnvoieVersClient()

MyServeur.__del__()