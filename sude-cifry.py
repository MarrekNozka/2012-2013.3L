#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  sude-cifry.py
# Datum:   22.11.2012 08:15
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Určete počet různých sudých cifer daného přirozeného čísla.
############################################################################

# načtu řetězec
radek = raw_input("zadej mi sem řetězec >> ")
print type(radek)

pocet = 0
i=0
while i<len(radek):
    z = radek[i]
    if z=='2' or z=='4' or z=='6' or z=='8':
        pocet = pocet + 1
    i += 1

if pocet ==1:
    bagr ="v tomto řetězci je {} sudá cifra"
elif pocet >=2 and pocet <=4 :
    bagr ="v tomto řetězci jsou {} sudé cifry"
else:
    bagr ="v tomto řetězci je {} sudých cifer"

print bagr.format(pocet)
