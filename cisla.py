#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  cisla.py
# Datum:   29.11.2012 09:09
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: Pro záporná čísla vypište na obrazovku jejich druhou mocninu. 
#        Pro kladná čísla vypište na obrazovku jejich odmocninu.
############################################################################

radek = raw_input('zadej čísla > ')

cisla = radek.split()
print cisla

i = 0
while i<len(cisla):
    cislo = float(cisla[i])
    if cislo>0 :
        # odmocnina
        # print cislo,'->', cislo**0.5
        print '{0:9f} -> {1:9f}'.format(cislo,cislo**0.5)
    else:
        # modnina
        # print cislo,'->', cislo**2
        print '{0:9f} -> {1:9f}'.format(cislo,cislo**2)
    i = i +1
