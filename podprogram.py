#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  podprogram.py
# Datum:   03.01.2013 09:07
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Jak je to s podprogramy, lokální a globální proměné
############################################################################


# podprogram bez pararametrů
def podA():
    x = 20
    print x
    x = 77

def podB():
    x = 60
    print x
    x = 88

def podG():
    global x
    print x
    x = 123

def podZ():
    print a

# podprogram s návratovou hodnoutou
def odmocnina(x,n):
    vysledek = x ** (1./n)
    return vysledek

################################################################
## Hlavní program

x = 66
podA()
podB()
podG()
print x

print '-------------------------------------------'
a = 44
podZ()

print '-------------------------------------------'
print odmocnina(16,4)
print odmocnina(64,2)
