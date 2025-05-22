# -*- coding: utf-8 -*-
"""
Created on Thu May 22 17:25:56 2025

@author: Alexa
"""

# "Eingabe der ersten Zahl"
Zahl1 = float(input("Bitte geben Sie die erste Zahl ein: "))

# "Eingabe der zweiten Zahl"
Zahl2 = float(input("Bitte geben Sie die zweite Zahl ein: "))

# "Auswertung des Ergebnisses"
Ergebnis = Zahl1 / Zahl2

# "Auswertung des Ergebnisses gerundet auf eine Ganzzahl"
Ergebnis2 = round(Zahl1 / Zahl2, 4)

Ergebnis = float(round(Ergebnis))


print(f'Das komplette Ergebnis ist, {Ergebnis}')
print(f'Das gerundete Ergebnis ist, {Ergebnis2}"')
