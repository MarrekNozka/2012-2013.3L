#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  pyramida.py
# Datum:   29.11.2012 08:18
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   tiskne pyramidu ze znaků
############################################################################

pRadku = input('zadej počet řádků > ')

pMezer = pRadku - 1
pZnaku = 1

i=0
while i<pRadku :
    i = i+1
    print pMezer*' ' + pZnaku*'*'
    pZnaku += 2
    pMezer -= 1

