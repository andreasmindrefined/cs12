# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:04:11 2025

@author: Alex
"""


#Übungsaufgabe 3

#Übergabe der Parameter
gruß = input("Bitte geben Sie ein, wie der Benutzer begrüßt werden soll: ")
name = input("Bitte geben Sie Ihren Namen ein: ")
alter = input("Bitte geben Sie Ihr Alter ein: ")


#Erstellung einer Funktion 
def begruessung(gruß, name, alter):
    print(gruß, name, alter, "Jahre")


#Aufruf der erstellten Funktion
begruessung(gruß, name, alter)

