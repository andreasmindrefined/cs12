# -*- coding: utf-8 -*-
"""
Created on Thu May 22 17:26:21 2025

@author: Admin
"""

Zahl1=float(input('Gib mir Zahl 1: '))
Zahl2=float(input('Gib mir Zahl 2: '))

Ergebnis = Zahl1 / Zahl2
Ergebnis2 = round(Zahl1 / Zahl2,4)
Ergebnis3 = float(round(Ergebnis2))

print(f'Das Ergebnis ist: {Ergebnis}')
print(f'Das Ergebnis auf 2 Stellen ist: {Ergebnis2}')
print(f'Das Ergebnis gerundet ist: {Ergebnis3}')