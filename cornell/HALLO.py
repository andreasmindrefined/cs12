# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:49:54 2025

@author: Cornell
"""

name = input("pls type your name: ")
clean_name = name.strip(".")
clean_name = clean_name.strip(" ")
clean_name = clean_name.upper()
print(f'Moin, {clean_name}')