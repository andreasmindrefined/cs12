# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:48:35 2025

@author: Alex
"""

"Normale Print Methode - Der Inhalt wird in der Konsole ausgegeben"
print("Das ist das zweite Programm")

name = input("Wie ist dein Nachname: ")
name2 = input("Wie ist dein Vorname: ")

"Eingaben werden formatiert: Alle Leerzeichen werden gelöscht und in die Variable gespeichert"
cleaned_name = name.strip(" ")
cleaned_name2 = name2.strip(" ")

"Eingaben werden erneut formatiert: Die erste Eingabe wird Großgeschrieben, während die zweite Eingabe komplett Kleingeschrieben wird"
cleaned_name = cleaned_name.upper()
cleaned_name2 = cleaned_name2.upper()


"Erweiterte Print Methode - Man kann mit f' Variablen benutzen um eine Nachricht auszugeben"
print(f'Hallo, Herr {cleaned_name} {cleaned_name2} !')

