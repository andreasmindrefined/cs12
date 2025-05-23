# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:40:55 2025

@author: User
"""

def main():
    zahl1 = 5
    zahl2 = 6
    ergebnis = taschenrechner_plus(zahl1, zahl2)
    
    taschenrechner_minus(ergebnis, zahl2)
    
def taschenrechner_plus(zahl1,zahl2):
    ergebnis=zahl1+zahl2
    
    return ergebnis
    
def taschenrechner_minus(zahl1,zahl2):
    ergebnis=zahl1-zahl2
        
    print(f'ergebnis)
    
    
main()