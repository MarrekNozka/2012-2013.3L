# -*- coding: utf8 -*-
# Soubor:  veVyuce.py
# Datum:   11.04.2013 08:35
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   MODUL pro demonstraci práce s moduly
###################################################3 

cisloPi = 3.1415

# funkce obsah má proměný počet parametrů
# tuto skutečnost oznamuje *
def obsah(*parametry):
#    print parametry
    vysledek=1
    i=0
    while i < len(parametry)  :
        vysledek = vysledek * parametry[i] 
        i += 1
    return vysledek

def pi():
    return cisloPi
