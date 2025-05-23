# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:45:16 2025

@author: Alexa
"""

#Taschenrechner Beispiel
def main():
    zahl1 = 1
    zahl2 = 2
    ergebnis = taschenrechner_plus(zahl1, zahl2)
    
    print(taschenrechner_minus(ergebnis,zahl2))
    

def taschenrechner_plus(zahl1, zahl2):
    ergebnis = zahl1+zahl2
    return ergebnis

def taschenrechner_minus(zahl1, zahl2):
    ergebnis = zahl1-zahl2
    print(ergebnis)
    

main()