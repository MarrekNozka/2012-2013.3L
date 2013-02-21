#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  obrazek.py
# Datum:   21.02.2013 08:47
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   cernobily obrazek
###################################################3 

import pylab as lab
import random

# výška a šířka
w=400
h=300

obr=[]
# přídávám řádky
for i in range(h):
    radek=[]
    # přídávám čísla do řádku
    for j in range(w):
        radek.append( random.randint(0,100) )
    obr.append(radek)

lab.imshow(obr, interpolation='none', cmap='gray')

lab.show()
