#!/usr/bin/python3

from Client import Client

MyClient = Client()

while True :
    userPrompt = input("> ")

    MyClient.EnvoieVersServeur(userPrompt)

    reponse = MyClient.ReceptionReponse()

    print(reponse)

MyClient.__del__()