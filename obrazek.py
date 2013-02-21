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

#### vytvořím bílé plátno
obr=[]
# přídávám řádky
for i in range(h):
    radek=[]
    # přídávám čísla do řádku
    for j in range(w):
        radek.append( 100 )
    obr.append(radek)


# projdu obrázek pixel po pixelu
for y in range(h):
    for x in range(w):
        if x**2 + y**2 < 200**2 :
            obr[y][x] = 0

for y in range(h):
    for x in range(w):
        if (x-100)**2 + (y-200)**2 < 30**2 :
            obr[y][x] = 50

for y in range(h):
    for x in range(w):
       hodnota =(x-300)**2 + (y-100)**2  
       if hodnota>= 80**2 and hodnota<=81**2:
            obr[y][x] = 50

lab.imshow(obr, interpolation='none', cmap='gray')

lab.show()
