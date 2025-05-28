# -*- coding: utf-8 -*-
"""
Created on Thu May 22 17:25:36 2025

@author: User
"""
#Aufgabe Division
#x= 10.0
#y= 3.0
#Ergebnis round 3.33
#Ergebnis f-str: 3.33


zahlx=int(input("Gib eine Zahl X ein:"))
zahly=int(input("Gib eine Zahl Y ein:"))

Ergebnis = zahlx/zahly
Ergebnis = round(Ergebnis, 2)
print('"Ergebnis gerundet auf 2 Stellen ist:"',Ergebnis)