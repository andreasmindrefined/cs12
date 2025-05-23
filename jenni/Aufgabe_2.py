# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:59:02 2025

@author: User
"""

def main():
    
    
    #y = float(input("Zahl eingeben "))
    y = abfrage()
    
    print(taschenrechner(y))
    
    
def taschenrechner(x):
    ergebnis = x ** 2
    
    return ergebnis
    
def abfrage():
    y = float(input("Zahl eingeben "))
    
    return y
    
    
    
main()