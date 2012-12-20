#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kolikSudych.py
# Datum:   20.12.2012 08:35
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: Je dána posloupnost celých kladných čísel. Určete kolik z nich je sudých.
############################################################################

import random
############################################################################

seznam = [ random.randint(1,100) for _ in range(10) ]
print seznam

pocet = 0
for cislo in seznam:
    if cislo % 2 == 0 :
        pocet += 1
print pocet
############################################################################

i = 0
pocet = 0
while i<len(seznam):
    cislo = seznam[i]
    if cislo % 2 == 0 :
        pocet += 1
    i +=1
print pocet
