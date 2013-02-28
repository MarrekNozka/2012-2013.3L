#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prumer.py
# Datum:   28.02.2013 08:32
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   průměr
############################################################################

import random

seznam = [random.randint(1,50) for _ in range(20)]

############################################################################

i=0
suma=0
while i<len(seznam):
    suma = suma + seznam[i]
    i+=1
print float(suma) / len(seznam)

############################################################################

suma=0
for i in range(len(seznam)):
    suma = suma + seznam[i]
print float(suma) / len(seznam)

############################################################################

suma=0
for prvek in seznam:
    suma = suma + prvek
print float(suma) / len(seznam)

############################################################################

print float(sum(seznam)) / len(seznam)
