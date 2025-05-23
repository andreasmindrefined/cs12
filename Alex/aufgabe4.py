# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:59:56 2025

@author: Alexa
"""


#Lösung schwer Andreas


#In der Main wird
def main():
    y = abfrage()
    print(quadrat(y))
    
def abfrage():
    y = float(input("Zahl eingeben: "))
 #Der Befehl "return" gibt die Variable frei für andere Funktionen. Somit kann diese Variable woanders aufgerufen werden
    return y
    
def quadrat(x):
    ergebnis = x ** 2
    return ergebnis

main()


"""
So kann man 2 Werte übergeben

#In der Main wird
def main():
    y,x = abfrage()
    print(quadrat(y))
    print(x)
    
def abfrage():
    y = float(input("Zahl eingeben: "))
    x = 5 
 #Der Befehl "return" gibt die Variable frei für andere Funktionen. Somit kann diese Variable woanders aufgerufen werden
    return y, x
    
def quadrat(x):
    ergebnis = x ** 2
    return ergebnis

main()

"""


"""
Lösung einfach Alex

#Übungsaufgabe 4 - Quadratifizierung

#Parameterübergabe
zahl1 = int(input("Bitte Zahl eins eingeben: "))
zahl2 = int(input("Bitte Zahl zwei eingeben: "))

#Definition der Funktionen
def main():
    print("Das Ergebnis lautet:", taschenrechner())   
    
    
def taschenrechner():
    rechnung = (zahl1 ** zahl2)
    return rechnung
    print(rechnung)
        
#Main Funktion aufrufen     
main()


Lösung schwer Alex
# Übungsaufgabe 4 – Quadratifizierung mit Parameterübergabe

def get_num(prompt):

   
   # Fragt so lange eine ganze Zahl ab, bis
   # eine gültige Eingabe macht,
   # und gibt sie als int zurück.


    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Das war keine ganze Zahl. Bitte nochmal.")

def taschenrechner(a, b):
    #Berechnet a hoch b und gibt das Ergebnis zurück.
    return a ** b

def main():
    zahl1 = get_num("Bitte Zahl eins eingeben: ")
    zahl2 = get_num("Bitte Zahl zwei eingeben: ")
    ergebnis = taschenrechner(zahl1, zahl2)
    print("Das Ergebnis lautet:", ergebnis)

if __name__ == "__main__":
    main()
"""


